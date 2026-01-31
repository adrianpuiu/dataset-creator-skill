# Code-Agnostic Dataset Extractor - Conversational Format Guide

This skill extracts training data from codebases in **two formats**:

## Format 1: Instruction-Input-Output (Default)

Used by the skill's main extraction workflow:

```json
{
  "instruction": "I need a tool that can scrape websites",
  "input": "",
  "output": "async def scrape_url(url: str) -> str: ..."
}
```

**Best for:**
- Simple instruction tuning
- Code completion models
- Non-conversational training

## Format 2: Conversational (OpenAI-Compatible)

Convert to this format for fine-tuning chat models:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are an expert programmer..."
    },
    {
      "role": "user",
      "content": "I need a tool that can scrape websites"
    },
    {
      "role": "assistant",
      "content": "```python\nasync def scrape_url(url: str) -> str: ...\n```"
    }
  ]
}
```

**Best for:**
- Fine-tuning Claude, GPT-4, or other chat models
- Multi-turn conversation training
- OpenAI API fine-tuning
- Conversational AI systems

---

## How to Convert

### Option 1: Using the Provided Script

```bash
# Basic usage
python3 convert_to_conversational.py \
  --input dataset.jsonl \
  --output dataset_conversational.jsonl

# With custom system prompt
python3 convert_to_conversational.py \
  --input dataset.jsonl \
  --output dataset_conversational.jsonl \
  --system-prompt "You are a Python expert who..."

# With verbose output
python3 convert_to_conversational.py \
  --input dataset.jsonl \
  --output dataset_conversational.jsonl \
  --verbose
```

### Option 2: In Python Code

```python
from convert_to_conversational import convert_entry_to_conversational

# Convert a single entry
conversational = convert_entry_to_conversational(
    instruction="I need a tool that can...",
    output="async def scrape_url(...)...",
    system_prompt="You are an expert programmer..."
)

print(json.dumps(conversational))
```

### Option 3: Batch Convert

```python
from convert_to_conversational import convert_file

stats = convert_file(
    input_path="dataset.jsonl",
    output_path="dataset_conversational.jsonl",
    system_prompt="Custom prompt here"
)

print(f"Converted {stats['converted']} entries")
```

---

## System Prompt Reference

The default system prompt is:

```
You are an expert programmer who writes clean, efficient, well-documented code. 
You understand multiple programming languages and frameworks. 
When asked to implement something, you provide complete, working code with 
appropriate imports and structure.
```

### Custom System Prompts for Different Use Cases

**For Financial/Data Analysis:**
```
You are a senior data scientist specializing in financial analysis. 
You write clear, well-commented Python code using pandas, numpy, and scikit-learn. 
You explain your approach and provide complete, production-ready solutions.
```

**For DevOps/Infrastructure:**
```
You are an experienced DevOps engineer with expertise in cloud platforms, 
containerization, and infrastructure automation. You write Terraform, Ansible, 
and Bash scripts that are secure, scalable, and well-documented.
```

**For Web Development:**
```
You are a full-stack web developer specializing in modern frameworks. 
You write clean, maintainable code following SOLID principles and best practices. 
You provide complete implementations with proper error handling.
```

---

## Workflow: Extract → Convert → Fine-tune

### Step 1: Extract with the Skill

```bash
# Use the skill to extract from a codebase
claude extract-dataset pydantic-deepagents/ > dataset.jsonl
```

### Step 2: Convert to Conversational

```bash
python3 convert_to_conversational.py \
  --input dataset.jsonl \
  --output dataset_conversational.jsonl
```

### Step 3: Fine-tune Your Model

**OpenAI API:**
```bash
openai api fine_tunes.create \
  -t dataset_conversational.jsonl \
  -m gpt-3.5-turbo
```

**Anthropic API (Claude):**
Use the conversational format with Claude's fine-tuning endpoints.

**Local Training (Hugging Face):**
```python
from datasets import load_dataset
from transformers import AutoModelForCausalLM, Trainer, TrainingArguments

dataset = load_dataset('json', data_files='dataset_conversational.jsonl')
# Train with transformers library
```

---

## Validation Checklist

Before fine-tuning, verify your conversational dataset:

```bash
# Check entry count
wc -l dataset_conversational.jsonl

# Validate JSON
python3 -c "
import json
with open('dataset_conversational.jsonl') as f:
    for i, line in enumerate(f):
        try:
            json.loads(line)
        except json.JSONDecodeError as e:
            print(f'Line {i+1}: {e}')
"

# Sample entries
head -1 dataset_conversational.jsonl | python3 -m json.tool

# Check message structure
python3 -c "
import json
with open('dataset_conversational.jsonl') as f:
    entry = json.loads(f.readline())
    print('Messages:', len(entry.get('messages', [])))
    for msg in entry.get('messages', []):
        print(f'  - {msg[\"role\"]}: {len(msg[\"content\"])} chars')
"
```

---

## Troubleshooting

**Problem:** Script fails with "Input file not found"
```
Solution: Provide absolute path or ensure file exists in current directory
```

**Problem:** Some entries are skipped
```
Solution: Check errors with --verbose flag, verify input format
```

**Problem:** Output file is empty
```
Solution: Verify input dataset has 'instruction' and 'output' fields
```

**Problem:** System prompt too long
```
Solution: Reduce system prompt length or use concise instructions
```

---

## Performance Tips

- **For large datasets (>10k entries):** Process in batches
- **For custom prompts:** Test on 100 entries first
- **For fine-tuning:** Aim for 100-1000 conversational examples minimum
- **For quality:** Validate 10% of converted entries manually

---

## References

- [SKILL.md](SKILL.md) - Full skill documentation
- [references/agent_patterns.md](references/agent_patterns.md) - Agent extraction patterns
- [references/enterprise_integrations.md](references/enterprise_integrations.md) - Enterprise integration patterns
