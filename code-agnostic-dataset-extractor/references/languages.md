# Language-Specific Syntax Mappings

## Python

### Syntax Patterns
```python
# Function
def function_name(param1: type, param2: type = default) -> return_type:
    """Docstring"""
    pass

# Async function
async def async_function() -> Awaitable:
    pass

# Class
class ClassName(ParentClass):
    def __init__(self, param):
        self.param = param

    @property
    def prop(self):
        return self._prop

# Import variations
from module import name
from module import name1, name2
from module import name as alias
import module
import module as alias

# Decorator
@decorator
@decorator_with_args(arg="value")
def function():
    pass

# Context manager
with resource as r:
    pass

# Exception handling
try:
    pass
except SpecificError as e:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass

# Dataclass
from dataclasses import dataclass

@dataclass
class DataClass:
    field: type
    field_with_default: type = default_value

# Type hints (Python 3.10+)
from typing import Optional, List, Dict, Union

x: int = 5
y: Optional[str] = None
z: List[int] = []
w: Dict[str, int] = {}
```

### Canonical Mapping
- `def` → function
- `async def` → async_function
- `class` → class
- `from/import` → import
- `@decorator` → decorator
- `try/except` → error_handling
- `with` → context_manager
- `@dataclass` → dataclass_definition
- `lambda` → lambda_function
- `yield` → generator

---

## JavaScript / TypeScript

### JavaScript Syntax
```javascript
// Function declaration
function functionName(param1, param2 = default) {
    return value;
}

// Arrow function
const arrowFunction = (param1, param2) => {
    return value;
};

// Async function
async function asyncFunction() {
    const result = await promise;
    return result;
}

// Class
class ClassName extends ParentClass {
    constructor(param) {
        super();
        this.param = param;
    }

    method() {
        return this.param;
    }

    get getter() {
        return this._private;
    }
}

// Private fields (ES2022)
class WithPrivate {
    #privateField;
}

// Import (ES6)
import { name1, name2 } from 'module';
import defaultExport from 'module';
import * as alias from 'module';
import { export as alias } from 'module';

// Export
export const name = value;
export default function() {}
export { name1, name2 };
export { name as alias };

// Try-catch
try {
    riskyOperation();
} catch (error) {
    handleError(error);
} finally {
    cleanup();
}

// Promise
new Promise((resolve, reject) => {
    resolve(value);
});

// Generator
function* generatorFunction() {
    yield value;
}

// Destructuring
const { a, b } = object;
const [first, second] = array;

// Spread
const newObj = { ...oldObj, newProp: value };
const newArr = [...oldArr, newItem];
```

### TypeScript Syntax
```typescript
// Interface
interface InterfaceName {
    required: string;
    optional?: number;
    method(): void;
    genericMethod<T>(arg: T): T;
}

// Type alias
type TypeName = string | number;
type Generic<T> = {
    value: T;
};

// Generic function
function genericFunction<T>(param: T): T {
    return param;
}

// Enum
enum EnumName {
    Value1,
    Value2 = "custom",
}

// Namespace
namespace NamespaceName {
    export function exported() {}
}

// Utility types
type Partial = Partial<Interface>;
type Required = Required<Interface>;
type Readonly = Readonly<Interface>;
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `function name()` | function |
| `const name = () => {}` | arrow_function |
| `async function()` | async_function |
| `class Name {}` | class |
| `interface Name {}` | interface |
| `type Name =` | type_alias |
| `import/from` | import |
| `export` | export |
| `try/catch` | error_handling |
| `new Promise()` | promise |
| `function*` | generator |
| `enum` | enum |

---

## Go

### Syntax Patterns
```go
// Function
func functionName(param1 type, param2 type) returnType {
    return value
}

// Method
func (r *ReceiverType) methodName(param type) returnType {
    return value
}

// Variadic function
func variadic(params ...type) {
    for _, p := range params {
    }
}

// Multiple return values
func multiReturn() (int, error) {
    return 0, nil
}

// Struct
type StructName struct {
    FieldName    type
    PrivateField type
    TaggedField  type `json:"field_name" db:"field_name"`
}

// Interface
type InterfaceName interface {
    MethodName(param type) returnType
    AnotherMethod() error
}

// Interface implementation
func (s *StructName) MethodName(param type) returnType {
    return value
}

// Goroutine
go functionName()

// Channel
ch := make(chan type)
ch <- value        // send
value := <-ch      // receive

// Select
select {
case value := <-ch:
    // handle value
case ch <- value:
    // handle send
default:
    // default case
}

// Defer
defer file.Close()
defer func() {
    cleanup()
}()

// Error handling pattern
result, err := function()
if err != nil {
    return err
}

// Import (factored)
import (
    "standard/package"
    "local/package"
    alias "other/package"
)

// Constants with iota
const (
    Const1 = iota
    Const2
    Const3
)
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `func name()` | function |
| `type Name struct {}` | struct |
| `type Name interface {}` | interface |
| `import` | import |
| `go func()` | goroutine |
| `defer` | defer_statement |
| `select` | select_statement |
| `make(chan)` | channel |
| `if err != nil` | error_handling |

---

## Rust

### Syntax Patterns
```rust
// Function
fn function_name(param: Type, param: Type) -> ReturnType {
    value
}

// Async function
async fn async_function() -> ResultType {
    Ok(value)
}

// Closure
let closure = |param: Type| -> Type { param * 2 };
let short_closure = |param| param * 2;

// Struct
struct StructName {
    field: Type,
    public_field: Type,
}

// Tuple struct
struct TupleStruct(Type, Type);

// Unit struct
struct UnitStruct;

// Enum
enum EnumName {
    Variant1,
    Variant2(Type),
    Variant3 { field: Type },
}

// Option and Result
let maybe: Option<T> = Some(value);
let result: Result<T, E> = Ok(value);

// Pattern matching
match value {
    Pattern1 => action1,
    Pattern2 => action2,
    _ => default_action,
}

// Impl block
impl StructName {
    fn associated_function() {}
}

impl Trait for StructName {
    fn trait_method(&self) {}
}

// Generics
fn generic<T>(param: T) -> T {
    param
}

// Lifetime
fn with_lifetime<'a>(s: &'a str) -> &'a str {
    s
}

// Macro attributes
#[derive(Debug, Clone)]
struct DeriveStruct;

#[macro_use]
extern crate serde;

// Use statement
use std::collections::HashMap;
use crate::module::Item;
use crate::module::{self, Item1, Item2};
use super::ParentItem;

// Error handling with ?
fn result() -> Result<T, Error> {
    let value = may_fail()?;
    Ok(transform(value))
}

// Iterator
let doubled: Vec<_> = items.iter().map(|x| x * 2).collect();
for item in items {
    // process item
}
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `fn name()` | function |
| `async fn` | async_function |
| `struct Name {}` | struct |
| `enum Name {}` | enum |
| `trait Name {}` | trait |
| `impl Trait` | impl_block |
| `use` | import |
| `match` | pattern_matching |
| `Option<T>` | optional_type |
| `Result<T, E>` | result_type |
| `#[attribute]` | attribute_macro |

---

## Java

### Syntax Patterns
```java
// Class
public class ClassName extends ParentClass implements Interface {
    // Field
    private Type field;

    // Constructor
    public ClassName(Type param) {
        this.field = param;
    }

    // Method
    public ReturnType methodName(ParamType param) {
        return value;
    }

    // Getter/Setter
    public Type getField() {
        return field;
    }

    public void setField(Type value) {
        this.field = value;
    }
}

// Interface
public interface InterfaceName {
    void method();
    default void defaultMethod() {}
    static void staticMethod() {}
}

// Enum
public enum EnumName {
    VALUE1, VALUE2, VALUE3;

    public void method() {}
}

// Annotation
@Annotation(name = "value")
@AnotherAnnotation
public void annotatedMethod() {}

// Exception handling
try {
    // code
} catch (SpecificException e) {
    // handle
} catch (Exception e) {
    // handle generic
} finally {
    // cleanup
}

// Generics
public class GenericClass<T> {
    public <U> void genericMethod(T param1, U param2) {}
}

// Lambda
list.forEach(item -> System.out.println(item));
list.stream()
    .filter(item -> item.predicate())
    .map(Item::transform)
    .collect(Collectors.toList());
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `class Name {}` | class |
| `interface Name {}` | interface |
| `enum Name {}` | enum |
| `@Annotation` | annotation |
| `try/catch` | error_handling |
| `->` | lambda_expression |
| `<T>` | generic_type |

---

## C/C++

### C++ Syntax
```cpp
// Function
returnType functionName(Type param1, Type param2 = default) {
    return value;
}

// Lambda
auto lambda = [](Type param) -> ReturnType {
    return value;
};

// Class
class ClassName : public ParentClass {
private:
    Type field;

public:
    ClassName(Type param) : field(param) {}

    ReturnType method() {
        return field;
    }
};

// Template
template<typename T>
T templateFunction(T param) {
    return param;
}

template<typename T>
class TemplateClass {
    T value;
public:
    T getValue() { return value; }
};

// Enum class
enum class EnumName {
    VALUE1,
    VALUE2
};

// Exception handling
try {
    throw std::runtime_error("error");
} catch (const std::exception& e) {
    std::cerr << e.what();
}

// Smart pointers
std::unique_ptr<Type> ptr = std::make_unique<Type>();
std::shared_ptr<Type> shared = std::make_shared<Type>();
```

### C Syntax
```c
// Function
returnType functionName(Type param1, Type param2);

// Struct
struct StructName {
    Type field1;
    Type field2;
};

struct StructName variable;

// Enum
enum EnumName {
    VALUE1,
    VALUE2
};

// Pointer
Type* ptr = &variable;
Type value = *ptr;

// Typedef
typedef struct StructName Alias;

// Preprocessor
#define CONSTANT value
#include <header.h>
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `returnType name()` | function |
| `class Name {}` | class |
| `struct Name {}` | struct |
| `template<T>` | template |
| `enum class` | enum |
| `[]() {}` | lambda |
| `try/catch` | error_handling |
| `#include` | include |

---

## Ruby

### Syntax Patterns
```ruby
# Method
def method_name(param, param: default)
  # body
end

# Class
class ClassName < ParentClass
  attr_reader :attribute
  attr_accessor :writable

  def initialize(param)
    @instance_var = param
  end

  def instance_method
    @instance_var
  end

  def self.class_method
  end
end

# Block
array.each do |item|
  puts item
end

# Lambda/Proc
lambda = ->(param) { param * 2 }
proc = Proc.new { |param| param * 2 }

# Exception handling
begin
  risky_operation
rescue SpecificError => e
  handle_error(e)
rescue StandardError => e
  handle_generic(e)
else
  # no exception
ensure
  # always run
end

# Module
module ModuleName
  def self.module_method
  end
end

# Symbol (commonly used)
:symbol_name
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `def name` | method |
| `class Name` | class |
| `module Name` | module |
| `do...end` | block |
| `-> {}` | lambda |
| `begin...rescue` | error_handling |
| `attr_reader` | attribute_accessor |

---

## PHP

### Syntax Patterns
```php
// Function
function functionName(Type $param, ?Type $nullable = null): ReturnType {
    return $value;
}

// Arrow function (PHP 7.4+)
$arrow = fn($param) => $param * 2;

// Class
class ClassName extends ParentClass implements Interface {
    public Type $property;

    public function __construct(Type $param) {
        $this->property = $param;
    }

    public function method(): ReturnType {
        return $this->property;
    }
}

// Trait
trait TraitName {
    public function traitMethod() {}
}

// Interface
interface InterfaceName {
    public function method(): ReturnType;
}

// Exception handling
try {
    riskyOperation();
} catch (SpecificException $e) {
    handleException($e);
} finally {
    cleanup();
}

// Namespace
namespace Vendor\Package {
    class ClassName {}
}

use Vendor\Package\ClassName;
use function Vendor\Package\functionName;
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `function name()` | function |
| `fn() =>` | arrow_function |
| `class Name {}` | class |
| `interface Name {}` | interface |
| `trait Name {}` | trait |
| `try/catch` | error_handling |
| `namespace` | namespace |

---

## Swift

### Syntax Patterns
```swift
// Function
func functionName(param: Type, param: Type = default) -> ReturnType {
    return value
}

// Closure
let closure = { (param: Type) -> ReturnType in
    return param * 2
}

// Short closure
let shortClosure = { $0 * 2 }

// Class
class ClassName: ParentClass, Protocol {
    var property: Type
    let constant: Type

    init(param: Type) {
        self.property = param
        self.constant = value
    }

    func method() -> ReturnType {
        return property
    }
}

// Struct
struct StructName: Protocol {
    var property: Type
}

// Enum
enum EnumName {
    case value1
    case value2(Type)
    case value3(param: Type)

    func method() {}
}

// Protocol
protocol ProtocolName {
    var property: Type { get set }
    func method()
}

// Extension
extension TypeName {
    func newMethod() {}
}

// Optional handling
if let value = optional {
    // use unwrapped value
}

guard let value = optional else {
    return
}

// Error handling
do {
    try riskyOperation()
} catch {
    handleError(error)
}
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `func name()` | function |
| `class Name {}` | class |
| `struct Name {}` | struct |
| `enum Name {}` | enum |
| `protocol Name {}` | protocol |
| `extension` | extension |
| `if let` | optional_binding |
| `do/catch` | error_handling |

---

## Kotlin

### Syntax Patterns
```kotlin
// Function
fun functionName(param: Type, param: Type = default): ReturnType {
    return value
}

// Single-expression function
fun add(a: Int, b: Int): Int = a + b

// Lambda
val lambda = { param: Type -> param * 2 }

// Class
class ClassName constructor(param: Type) : ParentClass() {
    val property: Type = param

    fun method(): ReturnType {
        return property
    }
}

// Data class
data class DataClass(
    val property: Type,
    val another: Type
)

// Sealed class
sealed class SealedClass {
    data class Subclass(val value: Int) : SealedClass()
    object Singleton : SealedClass()
}

// Interface
interface InterfaceName {
    fun method()
    fun methodWithDefault() { /* default */ }
}

// Object (singleton)
object ObjectName {
    fun method() {}
}

// Companion object
class ClassName {
    companion object {
        fun staticMethod() {}
    }
}

// When expression
when (value) {
    pattern1 -> action1
    pattern2 -> action2
    else -> defaultAction
}

// Null safety
val nullable: Type? = null
val nonNull: Type = nullable ?: defaultValue

// Extension function
fun TypeName.extensionFunction() {}
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `fun name()` | function |
| `class Name {}` | class |
| `data class` | data_class |
| `interface Name {}` | interface |
| `object` | object_declaration |
| `sealed class` | sealed_class |
| `when` | when_expression |
| `?.` | null_safe_call |
| `?:` | elvis_operator |

---

## Shell (Bash)

### Syntax Patterns
```bash
# Function
function_name() {
    local param=$1
    echo "$param"
}

# Alternative syntax
function function_name {
    echo "$1"
}

# Conditional
if [[ condition ]]; then
    commands
elif [[ condition ]]; then
    commands
else
    commands
fi

# Loop
for item in list; do
    echo "$item"
done

while [[ condition ]]; do
    commands
done

# Case statement
case "$variable" in
    pattern1)
        commands
        ;;
    pattern2|pattern3)
        commands
        ;;
    *)
        default_commands
        ;;
esac

# Variable
variable="value"
export VARIABLE="value"

# Command substitution
result=$(command)
result=`command`

# Pipeline
command1 | command2 | command3

# Redirect
command < input.txt
command > output.txt
command 2> error.txt
command >> output.txt

# Background job
command &
```

### Canonical Mapping
| Syntax | Category |
|--------|----------|
| `name() {}` | function |
| `if/then/fi` | conditional |
| `for/do/done` | for_loop |
| `while/do/done` | while_loop |
| `case/esac` | case_statement |
| `$()` | command_substitution |
| `|` | pipeline |
| `&` | background |
