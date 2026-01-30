# Instruction Templates for Code Patterns

This document provides instruction templates organized by pattern category for generating consistent training data.

## Function Patterns

### Basic Function
- "Define a function named {name}"
- "Create a function that {does_what}"
- "Write a function called {name} that takes {n} parameters"
- "Implement a function that returns {return_type}"

### Async Function
- "Create an async function that fetches data"
- "Define an asynchronous function with error handling"
- "Write an async function that processes items concurrently"
- "Implement an async function that awaits multiple promises"

### Arrow/Lambda Function
- "Create an arrow function that {action}"
- "Write a lambda function for {purpose}"
- "Define an inline function using arrow syntax"
- "Create a short lambda for {operation}"

### Generator Function
- "Define a generator function that yields values"
- "Create a generator using function syntax"
- "Write a generator that iterates over {collection}"
- "Implement a generator with lazy evaluation"

### Method
- "Add a method to the class that {does_what}"
- "Define an instance method named {name}"
- "Create a static method for {purpose}"
- "Implement a class method with {n} parameters"

### Higher-Order Function
- "Create a function that accepts a callback"
- "Write a function that returns another function"
- "Define a higher-order function for {purpose}"
- "Implement a function that takes a function as parameter"

## Class/Object Patterns

### Class Definition
- "Define a class named {name}"
- "Create a class with {n} properties"
- "Write a class that inherits from {parent}"
- "Implement a class with constructor and methods"

### Interface/Trait
- "Define an interface with {n} methods"
- "Create an interface that extends {other_interface}"
- "Write a trait with default implementation"
- "Define a protocol with required methods"

### Abstract Class
- "Create an abstract class with abstract methods"
- "Define a base class that cannot be instantiated"
- "Write an abstract class with concrete and abstract members"

### Data Class / Record
- "Define a dataclass with {n} fields"
- "Create a record type for {purpose}"
- "Write a data class with default values"
- "Define a struct with automatic trait implementations"

### Singleton
- "Implement the singleton pattern"
- "Create a class with only one instance"
- "Write a singleton with lazy initialization"

### Factory
- "Create a factory function for {type}"
- "Implement the factory pattern for creating objects"
- "Write a factory method that returns different types"

## Import/Export Patterns

### Import
- "Import a named export from a module"
- "Import {name} from {module}"
- "Import multiple exports from a library"
- "Import a module with an alias"

### Export
- "Export a named function"
- "Create a default export"
- "Export multiple items from a module"
- "Re-export from another module"

### Require (CommonJS)
- "Require a module and use its exports"
- "Import a CommonJS module"
- "Destructure imports from require"

## Type System Patterns

### Type Alias
- "Define a type alias for {type}"
- "Create a union type for {purpose}"
- "Write a type alias for complex type"
- "Define an intersection type"

### Generic Type
- "Create a generic function with type parameter"
- "Define a generic class with {n} type parameters"
- "Write a function with constrained generic"
- "Implement a generic interface with default type"

### Enum
- "Define an enum with {n} values"
- "Create an enumeration with associated values"
- "Write an enum with raw values"
- "Define a flags enum"

### Optional/Nullable Type
- "Define a property with optional type"
- "Create a nullable type for {purpose}"
- "Write a type that can be null or value"

### Union Type
- "Define a union type of {type1} and {type2}"
- "Create a type that accepts multiple types"
- "Write a discriminated union type"

## Control Flow Patterns

### Conditional
- "Write an if-else statement that checks condition"
- "Create a conditional expression"
- "Implement pattern matching with when/case"
- "Write a ternary operator expression"

### Loop
- "Create a for loop that iterates over collection"
- "Write a while loop with condition"
- "Implement a do-while loop"
- "Create a foreach loop"

### Switch/Match
- "Write a switch statement with multiple cases"
- "Create a pattern matching expression"
- "Implement a match statement with guards"
- "Write a case statement with default"

### Try-Catch
- "Add error handling with try-catch"
- "Implement try-catch-finally block"
- "Write error handling with specific exception types"
- "Create a try-catch that logs and re-throws"

### Throw/Raise
- "Throw an exception with message"
- "Raise an error with custom type"
- "Create and throw a custom exception"

## Data Structure Patterns

### Array/List Operations
- "Create a list with {n} elements"
- "Write code to map over array"
- "Filter array items based on condition"
- "Reduce array to single value"

### Dictionary/Map
- "Create a map/dictionary with key-value pairs"
- "Write code to iterate over map entries"
- "Access dictionary value with default"
- "Merge multiple dictionaries"

### Set
- "Create a set with unique values"
- "Perform set union/intersection/difference"
- "Check if value exists in set"

### Stack/Queue
- "Implement a stack using list"
- "Create a queue data structure"
- "Write code to push/pop from stack"

## Async Patterns

### Promise/Future
- "Create a promise that resolves after delay"
- "Write code to chain promises"
- "Handle promise rejection with catch"
- "Create a promise with executor function"

### Async/Await
- "Use async-await to handle promise"
- "Await multiple promises concurrently"
- "Write an async function with error handling"
- "Create an async waterfall pattern"

### Callback
- "Write a function that accepts a callback"
- "Implement error-first callback pattern"
- "Create a callback-based API"

### Observable/Stream
- "Create an observable that emits values"
- "Write code to subscribe to observable"
- "Transform stream with operators"

## Decorator/Annotation Patterns

### Decorator
- "Apply a decorator to a function"
- "Create a custom decorator"
- "Use decorator with parameters"
- "Chain multiple decorators"

### Annotation
- "Add an annotation to a class"
- "Create a custom annotation"
- "Use annotation with parameters"

### Macro
- "Apply a macro attribute"
- "Define a procedural macro"
- "Use derive macro for trait implementation"

## Property Patterns

### Getter/Setter
- "Create a property with getter"
- "Write a getter and setter for private field"
- "Define a computed property"
- "Create a property with observer"

### Private/Public
- "Declare private class member"
- "Create public API surface"
- "Use access modifiers for encapsulation"

### Readonly
- "Define a read-only property"
- "Create an immutable object"
- "Use const modifier"

## File/System Patterns

### File Read
- "Read a file synchronously"
- "Read file contents asynchronously"
- "Read file line by line"
- "Parse JSON from file"

### File Write
- "Write content to file"
- "Append data to file"
- "Write JSON to file"

### Path Operations
- "Get file extension from path"
- "Join path segments"
- "Resolve absolute path"
- "Get parent directory"

### Directory
- "Create directory if not exists"
- "List files in directory"
- "Recursively walk directory tree"

## Testing Patterns

### Test Definition
- "Write a unit test for function"
- "Create a test suite for class"
- "Define a test case with assertion"

### Setup/Teardown
- "Add setup code before test"
- "Create teardown/cleanup after test"
- "Use before/after hooks"

### Mock/Stub
- "Mock a function return value"
- "Create a spy for function calls"
- "Stub API response"

### Assertion
- "Assert that value equals expected"
- "Check that condition is true"
- "Verify exception was thrown"

## Configuration Patterns

### Environment Variable
- "Read environment variable"
- "Get config from environment with default"
- "Validate required environment variables"

### Config Object
- "Create a configuration object"
- "Load config from file"
- "Merge default and user config"

### CLI Argument
- "Parse command line arguments"
- "Define CLI options with defaults"
- "Create subcommand structure"

## String/Text Patterns

### Template String
- "Create a template string with variables"
- "Use string interpolation"
- "Build multi-line string literal"

### String Operations
- "Concatenate multiple strings"
- "Format string with placeholders"
- "Split string by delimiter"
- "Join array of strings"

### Regex
- "Match pattern in string"
- "Replace using regex"
- "Extract groups from match"

## Best Practices for Instructions

### DO:
- Start with action verbs (Create, Define, Write, Implement, Add, Use)
- Be specific about what the code should accomplish
- Include relevant details (function name, parameters, types)
- Keep instructions concise but complete
- Use language-agnostic terminology when possible

### DON'T:
- Use question format ("How do I...?")
- Be vague or ambiguous
- Include implementation details in instruction
- Use language-specific syntax in instruction
- Make instructions overly long

### Examples:

| Bad Instruction | Good Instruction |
|-----------------|------------------|
| "How do I loop over array?" | "Create a for loop that iterates over array elements" |
| "Make a function" | "Define a function that takes two numbers and returns their sum" |
| "Python async stuff" | "Create an async function that fetches data from an API" |
| "class with things" | "Define a class with a constructor and two methods" |
| "import something" | "Import a named export from a module" |

## Context in Input Field

When to include context in the `input` field:

1. **Required imports** - When the output depends on specific imports
2. **Type definitions** - When the output references custom types
3. **Setup code** - When the output is a continuation
4. **Helper functions** - When the output calls non-standard helpers

Example:
```json
{
  "instruction": "Create a function that processes user data",
  "input": "interface User {\n  id: string;\n  name: string;\n  email: string;\n}\n\nfunction logError(msg: string): void;",
  "output": "function processUser(user: User): void {\n  if (!user.email) {\n    logError('User missing email');\n    return;\n  }\n  // Process user...\n}"
}
```
