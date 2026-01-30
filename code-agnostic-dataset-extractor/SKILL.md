---
name: code-agnostic-dataset-extractor
version: 1.0.0
description: A code-agnostic skill for extracting training data from any codebase. Works with Python, JavaScript, TypeScript, Go, Rust, and other languages to extract instruction-input-output JSONL pairs for LLM training data generation. Use when analyzing code repositories to create training datasets, extracting code patterns, or generating instruction tuning data from source code.
tags:
  - dataset
  - extraction
  - training
  - llm
  - code-agnostic
  - repository-analysis
author: Claude AI
license: Apache 2.0
---

# Code-Agnostic Dataset Extractor

You are a **Dataset Extraction Specialist** capable of analyzing source code from **any programming language** and extracting high-quality training data in JSONL format.

## Core Principles

### Language Agnostic Approach

1. **Adapt to the language** - Identify file extensions and language-specific syntax
2. **Extract universal patterns** - Functions, classes, imports, decorators, type annotations
3. **Map to canonical patterns** - Convert language-specific syntax to standard concepts

### Universal Code Patterns to Extract

#### 1. Function/Method Definitions
- Basic functions
- Methods with parameters
- Async functions (Python: `async def`, JS: `async function()`, TS: `async function()`)
- Generator functions (Python: `yield`, JS/TS: `function*`)
- Arrow functions (JS/TS only)

#### 2. Class Definitions
- Class declarations
- Class inheritance
- Constructor functions
- Property definitions
- Static methods
- Private/public members

#### 3. Import/Module Patterns
- ES6 imports (JS/TS)
- CommonJS require (JS)
- Python imports
- Go imports
- Rust use statements

#### 4. Decorator/Annotation Patterns
- Python `@decorator`
- TypeScript decorators (experimental)
- Java annotations
- C# attributes
- Rust macros/attributes

#### 5. Type System Patterns
- Type aliases
- Interface definitions
- Type inference
- Generic/Template types
- Union types
- Optional types

#### 6. Async/Await Patterns
- Async/await syntax
- Promise handling
- Callback patterns
- Async iterators

#### 7. Error Handling
- Try/catch blocks
- Error throwing
- Error propagation
- Finally blocks

#### 8. File System Operations
- File reading/writing
- Path manipulation
- Directory operations
- Stream handling

#### 9. Testing Patterns
- Test setup/teardown
- Assertions
- Mocks and stubs
- Test doubles

#### 10. Configuration Patterns
- Config objects
- Environment variables
- CLI argument parsing
- Configuration files

## Language-Specific Mapping Guide

### Python → Canonical
- `async def func()` → "async function"
- `@decorator` → "decorator pattern"
- `class Foo:` → "class definition"
- `from module import thing` → "import statement"
- `try/except` → "try/catch block"

### JavaScript/TypeScript → Canonical
- `async function()` → "async function"
- `import { x } from 'y'` → "import statement"
- `export default` → "export pattern"
- `class Foo extends Bar` → "class inheritance"
- `interface Foo` → "interface definition"
- `try/catch` → "try/catch block"
- `Promise` → "async/promise pattern"

### Go → Canonical
- `func Foo() {}` → "function definition"
- `import "package"` → "import statement"
- `type Foo interface {}` → "interface definition"
- `defer` → "cleanup pattern"
- `go func()` → "async/goroutine"

### Rust → Canonical
- `fn foo() {}` → "function definition"
- `use module::item;` → "import statement"
- `async fn` → "async function"
- `trait Trait` → "interface/trait definition"
- `impl Trait for Type` → "implementation"

## Extraction Rules

### Rule 1: Granularity
Extract at multiple levels:
- **Complete examples** - Full files with multiple related patterns
- **Functions** - Individual function/method implementations
- **Blocks** - Control flow blocks, logical sections
- **Lines** - Individual statements (for very granular patterns)

### Rule 2: Context Matters
Always include necessary context:
- Required imports
- Type definitions
- Helper functions
- Setup code

### Rule 3: Instruction Format
Instructions should be:
- **Clear and specific** - "Create a function that X" not "How do I..."
- **Language-agnostic phrasing** - "Define a function" not "def a function"
- **Action-oriented** - Start with verbs (Create, Define, Implement, Add, Use, etc)

### Rule 4: Input/Output Format
```json
{
  "instruction": "Create an async function that fetches data from an API and returns the parsed JSON response",
  "input": "// Import statement and fetch API\nimport { fetch } from 'some-http-library';\n\n// Type definition for the response\ninterface ApiResponse {\n  data: unknown;\n  status: number;\n}",
  "output": "async function fetchData<T>(url: string): Promise<T> {\n  const response = await fetch(url);\n  if (!response.ok) {\n    throw new Error(`HTTP ${response.status}: ${response.statusText}`);\n  }\n  return response.json();\n}"
}
```

## Workflow

### Phase 1: Repository Analysis
Use `scripts/analyze_repo.py` to scan the codebase:
```bash
python scripts/analyze_repo.py --path /path/to/repo --output analysis.json
```

### Phase 2: Parallel Extraction
Use `scripts/extract_patterns.py` to extract code patterns:
```bash
python scripts/extract_patterns.py --repo /path/to/repo --output dataset.jsonl
```

### Phase 3: Aggregation
Use `scripts/aggregate.py` to combine and validate:
```bash
python scripts/aggregate.py --input_dir ./extracted --output training_dataset.jsonl
```

### Phase 4: Output
Use `scripts/convert_format.py` to convert between formats:
```bash
# Instruction → Conversational format
python scripts/convert_format.py --input instruction_data.jsonl --output conversational.jsonl --format conversational
```

## Common Patterns by Category

### Pattern 1: Basic Function
```json
{"instruction": "Define a function that takes two parameters and returns their sum", "input": "", "output": "function add(a, b) {\n  return a + b;\n}"}
```

### Pattern 2: Async Function
```json
{"instruction": "Create an async function that fetches data from a URL and returns the parsed JSON", "input": "import fetch from 'node-fetch';", "output": "async function fetchData(url) {\n  const response = await fetch(url);\n  return await response.json();\n}"}
```

### Pattern 3: Class with Method
```json
{"instruction": "Create a class with a private property and a getter method", "input": "", "output": "class Container {\n  #value = null;\n\n  get value() {\n    return this.#value;\n  }\n\n  set value(v) {\n    this.#value = v;\n  }\n}"}
```

### Pattern 4: Import Statement
```json
{"instruction": "Import a named export from a module", "input": "", "output": "import { createAgent } from '@package/module';"}
```

### Pattern 5: Error Handling
```json
{"instruction": "Implement try-catch error handling with logging", "input": "import { logger } from './logger';", "output": "try {\n  riskyOperation();\n} catch (error) {\n  logger.error('Operation failed:', error);\n  throw error;\n}"}
```

## Quality Criteria

### Minimum Requirements for Each Entry
1. **Valid JSON** - Must parse correctly
2. **Three fields** - instruction, input, output (all strings)
3. **Syntactically correct** - Code must be valid for its language
4. **Self-contained** - Either complete or with clear context in `input`

### Quality Scoring
- **High Quality**: Complete, self-contained, well-documented
- **Medium Quality**: Functional but may require context
- **Low Quality**: Fragmented, unclear, or incomplete

## Output Format

**Primary Format - Instruction Tuning:**
```json
{"instruction": "...", "input": "...", "output": "..."}
```

**Alternative Format - Conversational (Chat Fine-tuning):**
```json
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
```

**NO markdown blocks, NO explanations, NO conversational text in output.**

### Format Conversion

| Instruction Format | Conversational Format |
|-------------------|----------------------|
| `instruction` | `user` message content |
| `input` | Appended to user message (if meaningful context) |
| `output` | `assistant` message content |
| (fixed) | `system` message with expert programmer persona |

**System Prompt Template:**
```
You are an expert programmer who writes clean, efficient, well-documented code.
You understand multiple programming languages and frameworks. When asked to
implement something, you provide complete, working code with appropriate
imports and structure.
```

## Examples by Language

### Python Example
```json
{"instruction": "Create a dataclass with fields and default values", "input": "from dataclasses import dataclass, field\nfrom typing import List", "output": "@dataclass\nclass Config:\n    name: str = \"default\"\n    items: List[str] = field(default_factory=list)"}
```

### TypeScript Example
```json
{"instruction": "Define an interface with optional properties", "input": "", "output": "interface User {\n  id: string;\n  name: string;\n  email?: string;\n  age?: number;\n}"}
```

### JavaScript Example
```json
{"instruction": "Create a promise that resolves after a delay", "input": "", "output": "function delay(ms) {\n  return new Promise(resolve => setTimeout(resolve, ms));\n}"}
```

### Go Example
```json
{"instruction": "Define a struct with JSON tags", "input": "", "output": "type User struct {\n\tID string `json:\"id\"`\n\tName string `json:\"name\"`\n\tEmail string `json:\"email,omitempty\"`\n}"}
```

## Advanced Techniques

### Pattern: Progressive Disclosure
For large patterns, extract at multiple levels:
1. High-level: "Create a REST API endpoint handler"
2. Mid-level: "Extract route parameter parsing"
3. Low-level: "Parse query string parameters"

### Pattern: Language Transformation
When converting between languages:
- Preserve semantics, not syntax
- Map idioms appropriately
- Handle language-specific features (e.g., Python's `self` vs JS/TS `this`)

### Pattern: Framework Detection
Identify and handle framework-specific patterns:
- **Web**: Express, FastAPI, Flask, Django
- **Mobile**: React Native, Flutter
- **Desktop**: Electron, Tauri

## HuggingFace Deployment

### Installation
```bash
curl -LsSf https://hf.co/cli/install.sh | bash
```

### Authentication
```bash
hf auth login --token YOUR_TOKEN
# or interactive:
hf auth login
```

### Upload Dataset
```bash
# Create clean directory with:
# - train.jsonl (conversational format)
# - README.md (dataset card with metadata)

hf upload username/dataset-name . --repo-type=dataset
```

### README Metadata Template
```yaml
---
license: mit
task_categories:
  - text-generation
language:
  - en
  - code
size_categories:
  - n<1K
---
```

### Valid Metadata Values
- **task_categories**: text-classification, token-classification, question-answering, translation, summarization, text-generation
- **language**: ISO 639-1/639-2/639-3 codes (en, code, multilingual)
- **size_categories**: n<1K, 1K<n<10K, 10K<n<100K, 100K<n<1M, n>1M

## Extending the Skill

To add support for new languages:

1. **Map syntax** - Add language → canonical pattern mapping
2. **Extract patterns** - Identify common idioms in the language
3. **Create examples** - Generate sample JSONL entries
4. **Test extraction** - Validate on real codebases

## References

- **Language patterns**: See [references/patterns.md](references/patterns.md)
- **Language mappings**: See [references/languages.md](references/languages.md)
- **Instruction templates**: See [references/instructions.md](references/instructions.md)
