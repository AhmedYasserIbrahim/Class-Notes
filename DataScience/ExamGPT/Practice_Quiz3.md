# Quiz

## Question 1: Advantages and Drawbacks of Lambda Expressions and Functional Programming Tools

**Discuss the advantages and potential drawbacks of using Python's lambda expressions and functional programming tools like map, filter, and reduce. In your response, consider the following points:**

- Readability and Maintainability: How do lambda functions compare to traditional function definitions in terms of code readability and maintenance?
- Performance: What are the performance implications of using functional programming tools in Python compared to traditional loops or list comprehensions?
- Use Cases: Provide examples of scenarios where using lambda expressions and functional programming tools would be more advantageous than other approaches in Python.

---

**Your Answer:**
Lambda functions often make the code more concise, therefore improving the readability of the code, even though they may increase the complexity of the code if overused. Lambda functions are often used with throw-away functions that we use once only. So, when writing code that we plan to reuse later, we often prefer to use traditional functions instead of lambda functions for better maintainability.

Lambda functions are more efficient than traditional functions, and they are used for better computer speed if we plan to use the function once. However, for more complex functions, we use traditional functions instead.

Lambda expressions are often used with Python in case we write a throw-away function that will not be reused as lambda functions would be considered more efficient in that case and more readable. Lambda functions are also especially useful when dealing with higher-order functions such as map(), filter(), and reduce(). One example is using lambda functions to filter elements in a list based on a specific criterion.

---

## Question 2: Calculate Attendance Rate

**Task:** Write a Python function named `calculate_attendance_rate()` that calculates the attendance rate for a specific student.

**Your Code:**
```python
def calculate_attendance_rate(data, id):
    student = data[id]
    present = 0
    total = 0
    for day in student:
        if day == True:
            present += 1
        total += 1
        
    return present / total * 100

print(calculate_attendance_rate(attendance_records, '1002'))
```

---

## Question 3: Identify Students with Perfect Attendance

**Task:** Write a Python function named `find_perfect_attendance()` that takes the attendance records dictionary and returns a list of student IDs who have perfect attendance.

**Your Code:**
```python
def find_perfect_attendance(data):
    studentsRates = []
    for student in data:
        if calculate_attendance_rate(attendance_records, student) == 100:
            studentsRates.append(student)
            
    return studentsRates

print(find_perfect_attendance(attendance_records))
```

---

## Question 4: Calculate Average Attendance Rate for All Students

**Task:** Write a Python function named `average_attendance_rate()` that calculates the average attendance rate for all students using a list comprehension and a lambda expression.

**Your Code:**
```python
from functools import reduce

def average_attendance_rate(data):
    rates = [calculate_attendance_rate(attendance_records, x) for x in attendance_records] # Use list comprehension
    total = reduce(lambda acc, x: acc + x, rates, 0) # Use lambda expression
    return total / len(rates)

print(average_attendance_rate(attendance_records))
```

---

## Question 5: Summing Attendance by Grade Level

**Task:** Write a Python function named `total_attendance_by_grade()` that takes a nested dictionary where the keys are grade levels and the values are dictionaries of student attendance records. The function should sum the total number of days attended for each grade using a lambda expression.

**Your Code:**
```python
from functools import reduce

def attendance_per_grade(data):
    tups = []
    for grade in grade_attendance:
        total = 0
        for student in grade_attendance[grade]:
            total += reduce(lambda acc, x: acc + 1 if x == True else acc, grade_attendance[grade][student], 0) # Lambda expression here
        tups.append((grade, total))
    
    return tups

print(attendance_per_grade(grade_attendance))
