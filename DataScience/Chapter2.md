# Python Data Science Lecture Notes

## Functional Programming
- **Definition**: Deals with computations as mathematical functions; avoids mutable and changeable data.
- **Key Concepts**:
  - **First-Class Functions**: Functions treated as objects; can be assigned to variables or passed as parameters.
  - **Higher-Order Functions**: Functions that can take other functions as parameters or return them as outputs.
  - **Pure Functions**: Functions without side effects, commonly used.
  
## Type Casting
- **Method**: `int(x)` (unlike Java).

## Lambda Functions
- Used with `sort` and `sorted` to identify the sorting key.
- Example: `sorted(list, key=lambda x: x.attribute, reverse=True)`

## List Comprehension
- **Syntax**: `[expression for item in iterable if condition]`
- **Example**: `doubleEvens = [x*2 for x in range(10) if x%2==0]`

## Generator Expressions
- Similar to list comprehensions but written in parentheses `()`.
- Not stored in memory; used for single use.

## Map and Filter
- **Conversion**: Output must be converted to a list.
- **Map**: Can operate on elements from two lists.
- **Filter**: Commonly used with a list of dictionaries.

## Reduce
- Example: `reduce(lambda x, y: x if x > y else y, iterable)`

## Lists and Tuples
- Can contain mixed data types.
- **List Functions**:
  - `insert(index, value)`
  - `extend(iterable)`
  - `remove(value)`
  - `pop(index)`
  - `count(value)`
  - `index(value)`

- **Tuples**:
  - Default return type; immutable, hashable, and better performance.
  - **Tuple Unpacking**: Assigning values to named variables.
  - Example: `a, b, *_ = tuple` (use `_` to ignore values).

## Dictionaries
- Access methods:
  - `my_dict.items()`, `my_dict.keys()`, `my_dict.values()`
  - Safe access: `my_dict.get(key)`
- **Updating**: `my_dict.update({...})` to modify multiple values.
- **Use Cases**: Caching, mapping, handling JSON.
- **JSON**:
  - Format: `{"Name": "Ahmed"}`
  - Conversion: `json.dumps(dict)` and `json.loads(json_string)`

## Sets
- Defined with `{}`; unordered, unindexed, and unique.
- **Methods**:
  - `add(value)`, `remove(value)`, `discard(value)`
  - Operations: union, intersection, difference.
- **Membership Test**: `if "apple" in fruits`.

## Object-Oriented Programming (OOP)
- **Class Definition**: `class Car:`
- **Constructor**: `def __init__(self, ...)` (similar to `this` in Java).
- **Access Modifiers**:
  - Public: no underscore
  - Protected: one underscore
  - Private: two underscores, e.g., `self.__attribute`.

### Four Pillars of OOP
1. **Abstraction**: Hides lower-level details; provides a blueprint.
2. **Inheritance**: Child inherits attributes from the parent; supports multiple inheritance.
3. **Composition**: "Has-a" relationship (e.g., car and engine).
4. **Polymorphism**: Same method names behave differently based on subclass or parameters (overloading/overriding).

### Class Types
- **Static**: No instance information needed.
- **Class**: Takes `cls` as the first parameter.
- **Property**: Takes attributes.
