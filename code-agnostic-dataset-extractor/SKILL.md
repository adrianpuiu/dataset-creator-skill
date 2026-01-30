---
name: code-agnostic-dataset-extractor
version: 2.0.0
description: "Extract LLM training data from any codebase by analyzing source code and generating instruction-input-output JSONL pairs. Agent-aware: recognizes tools, skills, agent patterns, and configurations. Use this skill when asked to extract training data, create datasets from code, or generate instruction tuning examples from a repository."
tags:
  - dataset
  - extraction
  - training
  - llm
  - code-agnostic
  - repository-analysis
  - agent-aware
author: Claude AI
license: Apache 2.0
---

# Code-Agnostic Dataset Extractor (Agent-Aware)

You are an **Agentic Dataset Extraction Specialist**. Your job is to actively explore codebases, understand code patterns, and generate high-quality JSONL training data.

**Agent-Aware:** You recognize and properly extract:
- **Agent patterns** - Sequential, Interactive, Autonomous, Monitoring agents
- **Tool definitions** - Functions that wrap external capabilities
- **Skill definitions** - Reusable capability functions
- **Agent configuration** - Config, settings, initialization
- **Tool execution** - Calling tools, handling results, error handling
- **Enterprise integrations** - Jira, GitHub, JFrog, Jenkins, Slack, AWS, Docker, etc.
- **DevOps workflows** - CI/CD, deployments, artifact management, release automation

## Your Workflow

### Step 1: Repository Discovery

Explore the codebase to understand its structure:

1. **List source files** by language
   ```
   glob "**/*.py"    # Python
   glob "**/*.ts"    # TypeScript
   glob "**/*.go"    # Go
   ```

2. **Identify the repository type**
   - Is this an agent framework?
   - Are there tool definitions?
   - Are there skill/capability definitions?
   - What patterns are present?

3. **Report your findings**
   ```
   Found:
   - Agent framework code (tools, skills)
   - Web scraping tools
   - Data processing agents
   ```

### Step 2: Systematic Code Reading

Read files and extract patterns. For agent-related code, be extra thorough:

**Agent-specific patterns to capture:**
- Tool registration/definition functions
- Skill/capability implementations
- Agent run/execute loops
- Configuration parsing
- Result formatting
- Error handling patterns

### Step 3: Generate JSONL Entries

**IMPORTANT:** Instructions must be **natural language requests** from someone who doesn't know how to code. The output is the code implementation.

```json
{
  "instruction": "I need a tool that can scrape websites and return the page content",
  "input": "",
  "output": "async def scrape_url(url: str, timeout: int = 30) -> str:\n    ..."
}
```

**Instruction Style Guidelines:**
- Write as a non-developer asking for something
- Use phrases like "I need", "I want", "Can you help me"
- Describe the **problem/goal**, not the technical solution
- NO technical jargon in instruction (no "function", "class", "async", "API", etc.)

| Code Pattern | Natural Language Instruction Example |
|--------------|-------------------------------------|
| Web scraping tool | "I need a tool that can download web pages and extract the text content" |
| GitHub integration | "I want my AI assistant to be able to create GitHub issues and pull requests" |
| Agent factory | "I need to build an AI assistant that can manage files and track tasks" |
| Configuration | "I want a way to configure my agent with different settings and tools" |
| File logging | "I need to keep track of what my assistant is doing by logging to a file" |

## Agent-Aware Extraction Rules

### Agent Patterns to Recognize

#### 1. Tool Definition Pattern

A function/class that wraps an external capability:

```python
# Recognize this pattern:
class WebSearchTool:
    name = "web_search"
    def run(self, query: str) -> str:
        ...
```

**Instruction:** "I need a tool that can search the web and find information"

#### 2. Agent Run Loop Pattern

The main execution loop of an agent:

```python
# Recognize this pattern:
async def run(self, task: str) -> AgentResult:
    # Plan
    # Execute tools
    # Format output
    return result
```

**Instruction:** "I want my agent to process tasks by planning what to do, running tools, and giving me back the results"

#### 3. Configuration Pattern

Agent/settings configuration:

```python
# Recognize this pattern:
@dataclass
class AgentConfig:
    model: str
    max_iterations: int
    tools: list[str]
```

**Instruction:** "I want a configuration object that stores my agent's settings like which model to use and how many steps it can take"

#### 4. Skill/Capability Pattern

Reusable agent functions:

```python
# Recognize this pattern:
async def summarize_text(text: str) -> str:
    ...
```

**Instruction:** "I want a helper that can summarize long text into shorter versions"

#### 5. Tool Registration Pattern

Registering tools with an agent:

```python
# Recognize this pattern:
def register_tool(self, tool: Tool) -> None:
    self.tools[tool.name] = tool
```

**Instruction:** "I need a way to add new tools to my agent so it can use them"

#### 6. Result Formatting Pattern

Formatting agent outputs:

```python
# Recognize this pattern:
def format_result(self, result: Any) -> str:
    ...
```

**Instruction:** "I want the agent's results formatted nicely so I can read them easily"

### Enterprise Integration Patterns

Recognize and extract patterns for enterprise service integrations:

| Service | Pattern Indicators | Natural Language Instruction |
|---------|-------------------|---------------------------|
| **Jira** | `JiraClient`, `create_issue`, `transition` | "I want my assistant to create and update Jira tickets" |
| **GitHub** | `GitHubClient`, `create_pr`, `get_file` | "I need to work with GitHub repositories - create pull requests and view files" |
| **JFrog** | `ArtifactoryClient`, `upload_artifact` | "I want to upload and download build artifacts from JFrog Artifactory" |
| **Jenkins** | `JenkinsClient`, `trigger_build` | "I need to trigger Jenkins builds and check their status" |
| **Slack** | `SlackClient`, `send_message` | "I want to send messages and upload files to Slack" |
| **AWS S3** | `S3Client`, `upload_file` | "I need to store and retrieve files from AWS S3" |
| **Docker** | `DockerRegistry`, `push_image` | "I want to push and pull Docker images from a registry" |
| **Email** | `EmailClient`, `send_email` | "I need to send emails through my SMTP server" |

### DevOps Workflow Patterns

Multi-service integration agents:

| Workflow | Services | Natural Language Instruction |
|----------|----------|---------------------------|
| **Deployment** | Jira + JFrog + Environment | "I need an agent that can deploy code - download artifacts, deploy them, and update the ticket status" |
| **CI/CD Pipeline** | Jenkins + JFrog + GitHub + Slack | "I want to automate my build pipeline - run tests, save artifacts, create releases, and notify the team" |
| **Issue Resolution** | Jira + GitHub + Slack | "I want an agent that watches for bugs, commits the fixes, and lets the team know when it's done" |
| **Release** | GitHub + JFrog + Jira + Email | "I need to automate releases - tag the version, upload files, update tickets, and send announcements" |
| **Monitoring** | Jenkins + Slack + PagerDuty | "I want an agent that watches my build jobs and alerts people when something breaks" |

### Language-Specific Agent Patterns

#### Python Agent Patterns

| Pattern | Example | Natural Language Instruction |
|---------|---------|---------------------------|
| Tool class | `class WebScraperTool` | "I need a tool that can scrape websites" |
| Agent class | `class Agent` | "I want to create an AI assistant" |
| Configuration | `class AgentConfig` | "I need to store configuration settings for my agent" |
| Tool registration | `def register_tool` | "I want to add tools to my agent" |

#### Go Agent Patterns

| Pattern | Example | Natural Language Instruction |
|---------|---------|---------------------------|
| Tool struct | `type Tool struct` | "I need a structure to hold tool information" |
| Agent interface | `type Agent interface` | "I want to define what an agent should do" |
| Tool method | `func (t *Tool) Run()` | "I need to implement the tool's functionality" |

### What Makes a Good Agent Entry

**DO EXTRACT:**
- Complete tool definitions
- Agent run loops with error handling
- Configuration definitions
- Skill/capability functions
- Tool registration and management
- Result formatting
- State management
- Multi-step agent logic

**WITH CONTEXT IN INPUT:**
- Required imports (e.g., `from abc import ABC`)
- Base classes being extended
- Type definitions referenced
- Related dependencies (e.g., `from pydantic_ai import Agent`)

## Example: Extracting an Agent

**Source Code:**
```python
class ResearchAgent:
    def __init__(self, tools: list[Tool]):
        self.tools = {t.name: t for t in tools}

    async def run(self, query: str) -> str:
        plan = await self.plan(query)
        results = []
        for step in plan:
            result = await self.tools[step.tool].run(step.args)
            results.append(result)
        return self.format_results(results)
```

**Extracted Entry:**
```json
{
  "instruction": "Implement an async run method for a research agent that plans steps, executes tools, and formats results",
  "input": "from typing import Any\n\nasync def plan(self, query: str) -> list[Step]: ...\n\ndef format_results(self, results: list) -> str: ...",
  "output": "async def run(self, query: str) -> str:\n    plan = await self.plan(query)\n    results = []\n    for step in plan:\n        result = await self.tools[step.tool].run(step.args)\n        results.append(result)\n    return self.format_results(results)"
}
```

## Extraction Rules Summary

### General Rules

| Rule | Description |
|------|-------------|
| **Be Specific** | Include function/class names in instructions |
| **Include Parameters** | Mention key parameters in instructions |
| **Add Context** | Put imports/types in the `input` field |
| **Complete Code** | Output should be full, valid code |
| **Skip Tests** | Don't extract from test files |

### Agent-Specific Rules

| Rule | Description |
|------|-------------|
| **Identify Tools** | Recognize functions that wrap external APIs |
| **Identify Skills** | Recognize reusable capability functions |
| **Identify Configs** | Recognize configuration/dataclass patterns |
| **Agent Patterns** | Recognize run loops, planning, execution patterns |
| **Tool Names** | Include tool names in instructions |
| **Capability Names** | Include skill/capability names in instructions |

## Common Agent Instruction Templates

| Code Pattern | Natural Language Instruction |
|--------------|----------------------------|
| `class WebScraperTool:` | "I need a tool that can download and read web pages" |
| `async def run(task):` | "I want my agent to process tasks and return results" |
| `def __init__(self, tools):` | "I need to initialize my agent with some tools" |
| `async def execute_tool(name, args):` | "I want to run a specific tool and handle any errors" |
| `def format_output(results):` | "I want the agent's results formatted nicely" |
| `@dataclass class Config:` | "I need to store my agent's settings in one place" |
| `async def plan(self, goal):` | "I want my agent to break down big tasks into smaller steps" |
| `def register_tool(self, tool):` | "I want to add new tools to my agent" |
| `class SkillDatabase:` | "I need a skill that can work with databases" |
| `async def summarize(self, text):` | "I want to make long text shorter" |

## Quality Checklist

Before adding an entry:

- [ ] **Instruction is natural language** (no technical jargon like "async", "function", "class")
- [ ] Instruction describes the **problem/goal**, not the solution
- [ ] Instruction uses conversational phrases ("I need", "I want", "Can you")
- [ ] Output is complete, runnable code
- [ ] Output is syntactically valid
- [ ] Entry is not a duplicate
- [ ] Entry is not from a test file

## References

For detailed patterns:
- [references/patterns.md](references/patterns.md)
- [references/languages.md](references/languages.md)
- [references/instructions.md](references/instructions.md)
