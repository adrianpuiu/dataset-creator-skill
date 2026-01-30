---
name: code-agnostic-dataset-extractor
version: 2.0.0
description: Extract LLM training data from any codebase by analyzing source code and generating instruction-input-output JSONL pairs. Agent-aware: recognizes tools, skills, agent patterns, and configurations. Use this skill when asked to extract training data, create datasets from code, or generate instruction tuning examples from a repository.
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

Generate descriptive entries with agent-aware context:

```json
{
  "instruction": "Create a web scraping tool that takes a URL and returns the page content",
  "input": "from typing import Optional\nimport httpx\nfrom bs4 import BeautifulSoup",
  "output": "async def scrape_url(url: str, timeout: int = 30) -> str:\n    ..."
}
```

For agent patterns, use specific instructions:

| Pattern | Instruction Template |
|---------|---------------------|
| Tool definition | "Create a tool named {name} that {does_what} with {params}" |
| Agent run loop | "Implement the agent's run method that {does_what}" |
| Config class | "Define an agent configuration with {fields}" |
| Skill function | "Create a skill function for {capability} that takes {params}" |
| Tool execution | "Add a method to execute the {tool_name} tool with error handling" |

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

**Instruction:** "Create a tool named web_search that takes a query and returns search results"

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

**Instruction:** "Implement an async run method that takes a task, executes tools, and returns a formatted result"

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

**Instruction:** "Define an agent configuration dataclass with model, max_iterations, and tools fields"

#### 4. Skill/Capability Pattern

Reusable agent functions:

```python
# Recognize this pattern:
async def summarize_text(text: str) -> str:
    ...
```

**Instruction:** "Create a skill function named summarize_text that takes text and returns a summary"

#### 5. Tool Registration Pattern

Registering tools with an agent:

```python
# Recognize this pattern:
def register_tool(self, tool: Tool) -> None:
    self.tools[tool.name] = tool
```

**Instruction:** "Add a method to register a tool with the agent"

#### 6. Result Formatting Pattern

Formatting agent outputs:

```python
# Recognize this pattern:
def format_result(self, result: Any) -> str:
    ...
```

**Instruction:** "Create a method to format agent results as output"

### Enterprise Integration Patterns

Recognize and extract patterns for enterprise service integrations:

| Service | Pattern Indicators | Instruction Template |
|---------|-------------------|---------------------|
| **Jira** | `JiraClient`, `create_issue`, `transition` | "Create a Jira client with methods for creating and updating issues" |
| **GitHub** | `GitHubClient`, `create_pr`, `get_file` | "Create a GitHub client with methods for PRs, files, and operations" |
| **JFrog** | `ArtifactoryClient`, `upload_artifact` | "Create a JFrog Artifactory client with upload and download methods" |
| **Jenkins** | `JenkinsClient`, `trigger_build` | "Create a Jenkins client with methods to trigger builds and get status" |
| **Slack** | `SlackClient`, `send_message` | "Create a Slack client with message sending and file upload methods" |
| **AWS S3** | `S3Client`, `upload_file` | "Create an S3 client with upload, download, and list methods" |
| **Docker** | `DockerRegistry`, `push_image` | "Create a Docker registry client with push and pull methods" |
| **Email** | `EmailClient`, `send_email` | "Create an email client with SMTP sending capability" |

### DevOps Workflow Patterns

Multi-service integration agents:

| Workflow | Services | Instruction Template |
|----------|----------|---------------------|
| **Deployment** | Jira + JFrog + Environment | "Create a deployment agent that downloads artifacts from JFrog, deploys to environment, and updates Jira" |
| **CI/CD Pipeline** | Jenkins + JFrog + GitHub + Slack | "Create a CI/CD agent that runs Jenkins builds, pushes to JFrog, creates GitHub releases, and notifies on Slack" |
| **Issue Resolution** | Jira + GitHub + Slack | "Create an agent that monitors Jira issues, commits fixes via GitHub, and sends notifications on Slack" |
| **Release** | GitHub + JFrog + Jira + Email | "Create a release agent that creates GitHub tags, uploads artifacts to JFrog, updates Jira tickets, and sends email notifications" |
| **Monitoring** | Jenkins + Slack + PagerDuty | "Create a monitoring agent that watches Jenkins jobs and sends alerts via Slack and PagerDuty" |

### Language-Specific Agent Patterns

#### Python Agent Patterns

| Pattern | Example | Instruction Template |
|---------|---------|---------------------|
| Tool interface | `interface Tool` | "Define a tool interface with execute method" |
| Agent class | `class Agent { run() }` | "Create an agent class with async run method" |
| Tool definition | `const tool: Tool =` | "Define a tool object with name and handler" |
| Config type | `interface AgentConfig` | "Define an agent configuration type" |

#### Go Agent Patterns

| Pattern | Example | Instruction Template |
|---------|---------|---------------------|
| Tool struct | `type Tool struct` | "Define a tool struct with Name and Run fields" |
| Agent interface | `type Agent interface` | "Define an agent interface with Run method" |
| Tool function | `func (t *Tool) Run()` | "Implement the Run method for a tool" |

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

| Code Pattern | Instruction |
|--------------|-------------|
| `class WebScraperTool:` | "Create a tool class named WebScraperTool for scraping web pages" |
| `async def run(task):` | "Implement an async run method that processes a task" |
| `def __init__(self, tools):` | "Create an agent constructor that accepts a list of tools" |
| `async def execute_tool(name, args):` | "Create a method to execute a tool by name with error handling" |
| `def format_output(results):` | "Create a method to format agent results as output" |
| `@dataclass class Config:` | "Define an agent configuration dataclass" |
| `async def plan(self, goal):` | "Create an async planning method that breaks down goals into steps" |
| `def register_tool(self, tool):` | "Add a method to register a tool with the agent" |
| `class SkillDatabase:` | "Create a skill class for database operations" |
| `async def summarize(self, text):` | "Create a skill method to summarize text content" |

## Quality Checklist

Before adding an entry:

- [ ] Instruction is specific (includes function/class name)
- [ ] Instruction captures agent context (tool, skill, config, etc.)
- [ ] Input contains necessary imports
- [ ] Output is complete code
- [ ] Output is syntactically valid
- [ ] Entry is not a duplicate
- [ ] Entry is not from a test file

## References

For detailed patterns:
- [references/patterns.md](references/patterns.md)
- [references/languages.md](references/languages.md)
- [references/instructions.md](references/instructions.md)
