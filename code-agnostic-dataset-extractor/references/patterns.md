# Universal Code Patterns

This document defines canonical patterns that apply across programming languages for dataset extraction.

## Pattern Categories

### 1. Function Definition

**Canonical**: A named block of code that takes parameters and returns a value.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| Python | `def name(params):` | "Define a function named {name}" |
| JavaScript | `function name(params) {` | "Create a function called {name}" |
| TypeScript | `function name(params): type {` | "Define a typed function" |
| Go | `func name(params) return_type {` | "Create a function" |
| Rust | `fn name(params) -> type {` | "Define a function" |
| C++ | `return_type name(params) {` | "Declare a function" |
| Java | `return_type name(params) {` | "Define a method" |

### 2. Async Function

**Canonical**: A function that executes asynchronously and returns a promise/future.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| Python | `async def name(params):` | "Create an async function" |
| JavaScript | `async function name(params) {` | "Define an async function" |
| TypeScript | `async function name(params): Promise<T> {` | "Create an async typed function" |
| Go | `func name(params) <-chan type {` | "Create a goroutine channel" |
| Rust | `async fn name(params) -> impl Future {` | "Define an async function" |

### 3. Class Definition

**Canonical**: A template for creating objects with properties and methods.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| Python | `class Name:` | "Define a class" |
| JavaScript | `class Name {` | "Create a class" |
| TypeScript | `class Name {` | "Define a typed class" |
| Go | `type Name struct {` | "Define a struct" |
| Rust | `struct Name {` | "Define a struct" |
| C++ | `class Name {` | "Declare a class" |
| Java | `class Name {` | "Define a class" |

### 4. Interface / Trait

**Canonical**: A contract defining required methods and properties.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| TypeScript | `interface Name {` | "Define an interface" |
| Go | `type Name interface {` | "Define an interface" |
| Rust | `trait Name {` | "Define a trait" |
| Java | `interface Name {` | "Create an interface" |
| Python | `@abc.abstractmethod` | "Define an abstract base class" |

### 5. Import Statement

**Canonical**: Bringing in code from another module or library.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| Python | `from module import name` | "Import from a module" |
| JavaScript (ES6) | `import { name } from 'module'` | "Import a named export" |
| JavaScript (CJS) | `const name = require('module')` | "Require a module" |
| TypeScript | `import { name } from 'module'` | "Import with type info" |
| Go | `import "module"` | "Import a package" |
| Rust | `use module::item;` | "Use an item" |
| C++ | `#include <header>` | "Include a header" |

### 6. Decorator / Annotation

**Canonical**: Metadata that modifies or describes a function/class.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| Python | `@decorator` | "Use a decorator" |
| TypeScript | `@decorator()` | "Apply a decorator" |
| Java | `@Annotation` | "Add an annotation" |
| C# | `[Attribute]` | "Apply an attribute" |
| Rust | `#[attribute]` | "Use a macro attribute" |

### 7. Error Handling

**Canonical**: Handling exceptional conditions or errors.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| Python | `try: ... except Error as e:` | "Handle exceptions with try-except" |
| JavaScript | `try { ... } catch (e) {` | "Add error handling with try-catch" |
| TypeScript | `try { ... } catch (e) {` | "Handle errors with try-catch" |
| Go | `if err != nil { return err }` | "Handle Go-style errors" |
| Rust | `match result { Ok(v) => ..., Err(e) => ... }` | "Handle Result with pattern matching" |
| Java | `try { ... } catch (Exception e) {` | "Catch exceptions" |

### 8. Lambda / Arrow Function

**Canonical**: Anonymous function expression.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| Python | `lambda x: x * 2` | "Create a lambda function" |
| JavaScript | `x => x * 2` | "Create an arrow function" |
| TypeScript | `(x: number) => x * 2` | "Define a typed arrow function" |
| C++ | `[](auto x) { return x * 2; }` | "Create a lambda" |
| Rust | `\|x\| x * 2` | "Define a closure" |
| Go | `func(x int) int { return x * 2 }` | "Create an anonymous function" |

### 9. Generator

**Canonical**: Function that yields multiple values over time.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| Python | `def gen(): yield value` | "Create a generator function" |
| JavaScript | `function* gen() { yield value; }` | "Define a generator" |
| TypeScript | `function* gen() { yield value; }` | "Create a typed generator" |
| Rust | `fn gen() -> impl Iterator {` | "Return an iterator" |

### 10. Type Alias

**Canonical**: Giving a name to a type.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| TypeScript | `type Name = Type;` | "Define a type alias" |
| Python | `Name: Type = ...` | "Add type annotation" |
| Rust | `type Name = Type;` | "Create a type alias" |
| C++ | `using Name = Type;` | "Define a type alias" |
| Go | `type Name Type` | "Define a named type" |

### 11. Enum

**Canonical**: Type with fixed set of values.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| Python | `class Name(Enum):` | "Define an Enum" |
| TypeScript | `enum Name { ... }` | "Create an enum" |
| Rust | `enum Name { ... }` | "Define an enum" |
| Go | `const ( ... iota )` | "Define enumerated constants" |
| Java | `enum Name { ... }` | "Create an enum" |
| C++ | `enum class Name { ... }` | "Declare an enum class" |

### 12. Generic / Template

**Canonical**: Parameterized types.

| Language | Syntax | Template Instruction |
|----------|--------|---------------------|
| TypeScript | `function name<T>(param: T)` | "Create a generic function" |
| Rust | `fn name<T>(param: T)` | "Define a generic function" |
| Go | `func name[T any](param T)` | "Create a generic function" |
| Python | `def name(param: T):` | "Add generic type annotation" |
| Java | `<T> void name(T param)` | "Create a generic method" |
| C++ | `template<typename T> void name(T param)` | "Define a template function" |

## Composite Patterns

### 1. Promise Chain
```javascript
fetch(url)
  .then(res => res.json())
  .then(data => processData(data))
  .catch(err => handleError(err));
```
Instruction: "Chain promise operations with then and catch"

### 2. Async Iterator Loop
```python
async for item in async_iterable:
    await process(item)
```
Instruction: "Iterate over an async iterable"

### 3. Context Manager
```python
with open(path) as f:
    data = f.read()
```
Instruction: "Use a context manager for resource handling"

### 4. Singleton Pattern
```javascript
class Singleton {
    static instance = null;
    static getInstance() {
        if (!this.instance) this.instance = new Singleton();
        return this.instance;
    }
}
```
Instruction: "Implement the singleton pattern"

### 5. Observer Pattern
```python
class Observable:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, data):
        for obs in self.observers:
            obs.update(data)
```
Instruction: "Implement the observer pattern"

## Pattern Matching

### When extracting, match patterns to instructions:

| Code Pattern | Instruction Template |
|--------------|---------------------|
| `def name():` | "Define a function" |
| `class Name:` | "Create a class" |
| `import x` | "Import a module" |
| `try/catch` | "Add error handling" |
| `async def` | "Create an async function" |
| `lambda` | "Create a lambda function" |
| `@decorator` | "Apply a decorator" |
| `interface` | "Define an interface" |
| `type Name =` | "Create a type alias" |
| `enum Name {` | "Define an enumeration" |
