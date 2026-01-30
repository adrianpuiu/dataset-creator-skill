# Agent Patterns for Dataset Extraction

This reference defines agent-specific patterns to recognize when extracting training data from agent frameworks.

## Core Agent Components

### 1. Tool Definition

A tool wraps an external capability that an agent can use.

**Python Example:**
```python
class WebSearchTool:
    """Tool for searching the web."""

    name: str = "web_search"
    description: str = "Search the web for information"

    async def run(self, query: str, num_results: int = 5) -> list[dict]:
        """Execute the web search."""
        # Implementation
        pass
```

**Instruction:** "Create a tool class named WebSearchTool that searches the web and returns results"

**TypeScript Example:**
```typescript
interface Tool {
    name: string;
    description: string;
    execute(params: any): Promise<any>;
}

class SearchTool implements Tool {
    name = "web_search";
    description = "Search the web";

    async execute(params: { query: string }) {
        // Implementation
    }
}
```

### 2. Agent Class / Runner

The main agent that orchestrates tool execution.

**Python Example:**
```python
class Agent:
    def __init__(self, tools: list[Tool], llm: LLM):
        self.tools = {t.name: t for t in tools}
        self.llm = llm

    async def run(self, prompt: str) -> str:
        """Run the agent on a prompt."""
        # Generate plan
        plan = await self.llm.complete(f"Plan: {prompt}")

        # Execute tools
        results = []
        for step in plan.steps:
            result = await self.tools[step.tool].run(step.params)
            results.append(result)

        # Format output
        return self.format_output(results)
```

**Instruction:** "Implement an async run method that plans steps, executes tools, and formats results"

**TypeScript Example:**
```typescript
class Agent {
    private tools: Map<string, Tool>;

    constructor(tools: Tool[]) {
        this.tools = new Map(tools.map(t => [t.name, t]));
    }

    async run(prompt: string): Promise<string> {
        // Agent logic
    }
}
```

### 3. Configuration

Agent configuration settings.

**Python Example:**
```python
@dataclass
class AgentConfig:
    """Configuration for an agent."""
    name: str
    model: str = "claude-sonnet-4"
    temperature: float = 0.7
    max_tokens: int = 4096
    max_iterations: int = 10
    tools: list[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate the configuration."""
        return self.model in SUPPORTED_MODELS
```

**Instruction:** "Define an agent configuration dataclass with name, model, temperature, and tools fields"

### 4. Skill / Capability

Reusable functions that provide capabilities to the agent.

**Python Example:**
```python
class ResearchSkills:
    """Skills for research tasks."""

    @staticmethod
    async def summarize(text: str, max_length: int = 200) -> str:
        """Summarize text to a maximum length."""
        # Summarization logic
        pass

    @staticmethod
    async def extract_urls(text: str) -> list[str]:
        """Extract URLs from text."""
        import re
        return re.findall(r'https?://[^\s]+', text)
```

**Instruction:** "Create a skill class with a summarize method and an extract_urls method"

### 5. Tool Registry

Managing available tools.

**Python Example:**
```python
class ToolRegistry:
    """Registry of available tools."""

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        """Register a new tool."""
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        """Get a tool by name."""
        return self._tools.get(name)

    def list_tools(self) -> list[str]:
        """List all available tool names."""
        return list(self._tools.keys())
```

**Instruction:** "Create a tool registry class with register, get, and list_tools methods"

### 6. Planning

Agent planning and step decomposition.

**Python Example:**
```python
@dataclass
class Step:
    """A single execution step."""
    tool: str
    params: dict[str, Any]
    description: str

@dataclass
class Plan:
    """An execution plan."""
    steps: list[Step]

    def add_step(self, tool: str, params: dict, description: str) -> None:
        """Add a step to the plan."""
        self.steps.append(Step(tool, params, description))

class Planner:
    """Creates execution plans."""

    async def create_plan(self, goal: str) -> Plan:
        """Create a plan to achieve the goal."""
        # Plan generation logic
        pass
```

**Instruction:** "Create a planner class with an async create_plan method that returns a Plan"

### 7. Result Formatting

Formatting agent outputs.

**Python Example:**
```python
class ResultFormatter:
    """Formats agent results."""

    def format_markdown(self, results: list[dict]) -> str:
        """Format results as markdown."""
        lines = []
        for i, result in enumerate(results, 1):
            lines.append(f"## Step {i}: {result.get('description', '')}")
            lines.append(f"```\n{result.get('output', '')}\n```")
        return "\n".join(lines)

    def format_json(self, results: list[dict]) -> str:
        """Format results as JSON."""
        import json
        return json.dumps(results, indent=2)
```

**Instruction:** "Create a result formatter class with format_markdown and format_json methods"

### 8. Memory / State Management

Agent memory and context.

**Python Example:**
```python
@dataclass
class AgentMemory:
    """Agent working memory."""
    conversation_history: list[dict] = field(default_factory=list)
    tool_results: dict[str, Any] = field(default_factory=dict)
    context: dict[str, Any] = field(default_factory=dict)

    def add_message(self, role: str, content: str) -> None:
        """Add a message to history."""
        self.conversation_history.append({"role": role, "content": content})

    def store_result(self, key: str, value: Any) -> None:
        """Store a tool result."""
        self.tool_results[key] = value

    def get_context(self, key: str, default: Any = None) -> Any:
        """Get a context value."""
        return self.context.get(key, default)
```

**Instruction:** "Create an agent memory class with conversation history, tool results, and context storage"

### 9. Error Handling

Agent error handling patterns.

**Python Example:**
```python
class AgentError(Exception):
    """Base exception for agent errors."""
    pass

class ToolExecutionError(AgentError):
    """Raised when a tool fails."""
    def __init__(self, tool_name: str, original_error: Exception):
        self.tool_name = tool_name
        self.original_error = original_error
        super().__init__(f"Tool '{tool_name}' failed: {original_error}")

async def execute_tool_safely(
    tool: Tool,
    params: dict,
    on_error: str = "continue"
) -> Any | None:
    """Execute a tool with error handling."""
    try:
        return await tool.run(params)
    except Exception as e:
        if on_error == "raise":
            raise ToolExecutionError(tool.name, e)
        elif on_error == "return_none":
            return None
        else:
            return {"error": str(e), "tool": tool.name}
```

**Instruction:** "Create an async function to execute tools safely with configurable error handling"

### 10. Multi-Agent Orchestration

Coordinating multiple agents.

**Python Example:**
```python
class MultiAgentOrchestrator:
    """Orchestrates multiple agents."""

    def __init__(self, agents: list[Agent]):
        self.agents = agents

    async def run(self, task: str, agent_selector: str = "auto") -> str:
        """Run a task with the appropriate agent."""
        if agent_selector == "auto":
            # Select best agent
            agent = await self.select_agent(task)
        else:
            agent = self.agents[int(agent_selector)]

        return await agent.run(task)

    async def select_agent(self, task: str) -> Agent:
        """Select the best agent for a task."""
        # Selection logic
        return self.agents[0]
```

**Instruction:** "Create a multi-agent orchestrator class that manages multiple agents and routes tasks"

## Common Agent Frameworks

### LangChain Patterns

```python
# Tool definition
from langchain.tools import tool

@tool
def web_search(query: str) -> str:
    """Search the web for information."""
    # Implementation
    pass

# Agent definition
from langchain.agents import AgentExecutor, create_openai_functions_agent

agent = AgentExecutor(
    agent=create_openai_functions_agent(llm, tools),
    tools=tools,
    verbose=True
)
```

### PydanticAI Patterns

```python
from pydantic_ai import Agent

researcher = Agent(
    'researcher',
    tools=[web_search, file_reader],
)

result = researcher.run(
    "Research the latest AI developments"
)
```

### Custom Framework Patterns

```python
class SimpleAgent:
    """A simple agent framework."""

    def __init__(self, tools: dict):
        self.tools = tools
        self.memory = {}

    def run(self, prompt: str) -> str:
        # Simple single-shot execution
        tool_name, params = self.parse_request(prompt)
        result = self.tools[tool_name](**params)
        return self.format_result(result)
```

## Pattern Recognition Tips

When extracting, look for these keywords and patterns:

| Keyword/Pattern | Likely Agent Component |
|-----------------|------------------------|
| `class.*Tool` | Tool definition |
| `async def run` | Agent main loop |
| `def execute_tool` | Tool execution |
| `@tool` | Decorator-based tool |
| `register.*tool` | Tool registry |
| `AgentConfig` | Configuration |
| `def plan` | Planning |
| `memory` or `state` | State management |
| `format.*result` | Result formatting |
| `orchestrat` | Multi-agent |

## Extraction Examples

### Tool Definition Extraction

**Source:**
```python
class DatabaseTool:
    name = "database_query"

    def run(self, query: str) -> list[dict]:
        return self.db.execute(query)
```

**JSONL:**
```json
{
  "instruction": "Create a tool class named DatabaseTool that executes database queries",
  "input": "",
  "output": "class DatabaseTool:\n    name = \"database_query\"\n\n    def run(self, query: str) -> list[dict]:\n        return self.db.execute(query)"
}
```

### Agent Run Loop Extraction

**Source:**
```python
async def run(self, prompt: str) -> str:
    steps = await self.plan(prompt)
    outputs = []
    for step in steps:
        output = await self.execute_step(step)
        outputs.append(output)
    return "\n\n".join(outputs)
```

**JSONL:**
```json
{
  "instruction": "Implement an async run method that plans steps, executes each step, and concatenates outputs",
  "input": "",
  "output": "async def run(self, prompt: str) -> str:\n    steps = await self.plan(prompt)\n    outputs = []\n    for step in steps:\n        output = await self.execute_step(step)\n        outputs.append(output)\n    return \"\\n\\n\".join(outputs)"
}
```

### Config Extraction

**Source:**
```python
@dataclass
class AgentConfig:
    name: str
    model: str = "gpt-4"
    max_steps: int = 10
    tools: list[str] = field(default_factory=list)
```

**JSONL:**
```json
{
  "instruction": "Define an agent configuration dataclass with name, model, max_steps, and tools fields",
  "input": "from dataclasses import dataclass, field",
  "output": "@dataclass\nclass AgentConfig:\n    name: str\n    model: str = \"gpt-4\"\n    max_steps: int = 10\n    tools: list[str] = field(default_factory=list)"
}
```
