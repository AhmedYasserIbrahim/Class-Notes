# Racket Practice Log

## Introduction
This document summarizes my practice sessions with Racket v8.14, including various functions and expressions.

## Code Examples

### Basic Display
```racket
(display "Hello")
```
Output: `Hello`

### Proper List Display
```racket
(display '(1 2 3))
```
Output: `(1 2 3)`

### Creating a List with `list`
```racket
(display (list 1 2 3))
```
Output: `(1 2 3)`

### Lambda Function Example
```racket
(display ((lambda (x) (* x x)) 2))
```
Output: `4`

### Using a Lambda with Multiple Parameters
```racket
(display ((lambda (x y) (+ (* (+ x y) x) y)) 3 4))
```
Output: `21`

### Mathematical Operations
```racket
(display (* (+ (* 3 4) 3) 3))
```
Output: `45`

### Using `max`
```racket
(display (max 3 8 1 10))
```
Output: `10`

### Using `abs` and `max`
```racket
(display (* (max (abs -1) 3 8) 4))
```
Output: `32`

### Displaying a List
```racket
(define mylist (list 1 2 3 4))
(display mylist)
```
Output: `(1 2 3 4)`

### Correct Function Definition for Square
```racket
(define (square x) (* x x))
(display (square 5))
```
Output: `25`

### Product Function
```racket
(define (prod x y) (* x y))
(display (prod 3 4))
```
Output: `12`

### Using `cons`
```racket
(display (cons 1 (list 2 3 4)))
```
Output: `(1 2 3 4)`

### Using `append`
```racket
(define evens (list 0 2 4 6 8 10))
(define odds (list 1 3 5 7 9))
(define end (list "x"))
(display (append evens odds end))
```
Output: `(0 2 4 6 8 10 1 3 5 7 9 "x")`

### Using Logical Expressions
```racket
(display (or (>= 3 4) (string>? "Zain" "Ahmed")))
```
Output: `#t`

### Checking Boolean Condition
```racket
(display (bool? (> (* 2 3) 6)))
```
Output: `#t`

### Comparing Lists
```racket
(display (equal? evens odds))
```
Output: `#f`

### Checking for Null
```racket
(display (null? '()))
```
Output: `#t`

### Conditional Formatting Function
```racket
(define (conditionalFormat x)
  (if (> x 0)
      (display "Your number is greater than 0, the condition is true")
      (display "Your number is smaller than 0, the condition is false")))
(conditionalFormat 1)  ; Calls the function with 1 as an argument
```

### Conditional Format Using `cond`
```racket
(define (CONDformat x)
  (cond
    ((> 5 10) "First")
    ((not (= 0 0)) "Second")
    ((> (+ x 1) 0) "Third")))
(display (CONDformat 0))
```
Output: `"Third"`

### Summing All Elements in a List
```racket
(define (sumall nums)
  (if (null? nums)
      0  ; Return 0 directly when the list is empty
      (+ (car nums) (sumall (cdr nums)))))  ; Recursive case
(display (sumall (list 0 5 10 15)))
```
Output: `30`

### Factorial Function
```racket
(define (factorial x)
  (if (= x 0)
      1
      (* x (factorial (- x 1)))))
(display (factorial 5))
```
Output: `120`

## Notes on Errors Encountered

1. **Using Comma in List Creation**:
   - Incorrect: `(display (1,2,3))`
   - Correct: Use spaces instead of commas: `(display '(1 2 3))`

2. **Undefined Variable in Lambda**:
   - Error: `y: undefined`
   - Reason: Attempted to reference `y` before defining it in the lambda. Ensure all parameters are defined.

3. **Using `max` with a List**:
   - Incorrect: `(display (max (list 3 8 1 10)))`
   - Correct: Use individual arguments: `(display (max 3 8 1 10))`

4. **Defining a Function with Undefined Variable**:
   - Incorrect: `(define square (* x x))`
   - Correct: Define the function with its parameter: `(define (square x) (* x x))`

5. **Missing `else` Clause**:
   - Incorrect: In the `sumall` function, `(if (null? nums) (0))`
   - Correct: Always include an else clause: `(if (null? nums) 0 ...)`

6. **Misuse of `else` in Factorial**:
   - Incorrect: `else (* x (factorial (- x 1)))`
   - Correct: Just use `(if (= x 0) 1 (* x (factorial (- x 1))))`

By addressing these errors and understanding the corrections, I’ve improved my grasp of Racket programming.
```
