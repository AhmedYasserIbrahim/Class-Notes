# Data Science Class Notes

## Python Overview
- **Python**: Interpreted, multi-purpose programming language with dynamic semantics.
- **.whl**: Used for faster execution, compatibility, and ease.
- **Memory Management**: Automatic allocation to variables upon creation.

## Functional Programming (FP)
- **Definition**: Treats computations as evaluations of mathematical functions.
- **Advantages**:
  - Safe data handling
  - Easy-to-use tools
  - Clear workflow and predictability
  - Concurrency support
- **Key Concepts**:
  - **Modularity**: Writing code as smaller modules.
  - **Composability**: Combining modules to build complex systems.
- **Use Cases**: Large-scale data processing, academic settings.

### Pure Functions
- **Characteristics**: Deterministic (same input = same output), no side effects.
- **Advantages**: Predictability, reusability, concurrency.

### Higher Order Functions
- **Advantages**: Modularity, flexibility, reusability.

## Iterables and Iterators
- **Iterable**: Object that returns an iterator.
- **Iterator**: Tool for traversing an iterable's members.

## Lambda Functions
- **Use**: Quick computations, single-use, sorting.
- **Benefits**: Better readability and efficiency.

## Closures
- **Characteristics**:
  - Memory retention (context)
  - Encapsulation (data protection)

## List Comprehension
- **Advantages**: Conciseness, readability, efficiency.

## Generators
- **Definition**: List comprehensions for single-use, do not store values in memory.
- **Advantages**: Better performance and memory efficiency.

## Functional Tools
- **map()**:
  - Advantages: Efficiency, versatility, cleanliness.
  - Better for large datasets (memory efficient).
- **filter()**:
  - Advantages: Efficiency, versatility, cleanliness.
  - Better for large datasets (memory efficient) with simpler conditions.
- **reduce()**:
  - Advantages: Efficiency, compactness, flexibility.
  - Used with simpler cases than loops for better memory efficiency.

## JSON
- **Definition**: Immutable data exchange format.
- **Use**: Storing data in a readable format and transmitting data over networks.
- **Data Types**: Only allows string data types.

## Built-in Data Structures
- **Lists**: Mutable, ordered sequences; ideal for iterative modifications and mixed types.
- **Tuples**: Immutable; ensure data integrity and faster for constant datasets.
- **Sets**: Mutable, unordered; prevent duplicates, ideal for membership testing.
- **Dictionaries**: Key-value pairs; fast retrieval, ideal for associative arrays.

### Performance Considerations
- **Lists & Dictionaries**: Dynamic memory usage during insertions/deletions.
- **Tuples**: Lower memory footprint due to immutability.
- **Sets**: Average O(1) complexity for lookups using hash tables.

### Use Cases
- **List**: Data order required (e.g., maintaining records).
- **Tuple**: Read-only data (e.g., geographic coordinates).
- **Set**: Unique collections (e.g., tagging systems).
- **Dictionary**: Key-based retrieval (e.g., price lookups).

## Set Algebra
- **Operations**: Union, intersection, difference, symmetric difference.

## Object-Oriented Programming (OOP)
- **Pillars**: Encapsulation, abstraction, inheritance, polymorphism.
- **Concept**: Code reuse to mimic real-life object behavior.
- **Method Types**:
  - **Instance Methods**: Operate on class instances.
  - **Class Methods**: Operate on the class itself (`cls`).
  - **Static Methods**: Do not require class or instance data.
- **Access Modifiers**: Public, protected, private.
- **Composition**: Represents a "has-a" relationship.
- **Method Overriding**: Modifies inherited methods in subclasses.
- **Method Overloading**: Differentiates methods by parameters.
- **Property Method**: Similar to a getter.
- **Special Constructors**: 
  - `__init__`: Default constructor
  - `__str__`: String representation
  - `__len__`: Length of object
- **Class Design Principle**: Open for extension, closed for modification.
