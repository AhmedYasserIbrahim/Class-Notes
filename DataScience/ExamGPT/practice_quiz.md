## Q1: Lambda Functions in Python

**Question:**  
In Python, lambda functions are often used with higher-order functions like `map()`, `filter()`, and `reduce()`. Consider the readability and efficiency of lambda functions in comparison to traditional function definitions. Discuss a scenario where using a lambda function would be more advantageous than defining a regular function. Explain your reasoning clearly and concisely.

**Answer:**  
Lambda functions are anonymous, single-line functions that enhance readability in simple cases, such as implementing conditions and performing basic computations. They are particularly useful with higher-order functions and list comprehensions, reducing complexity. However, for more complex logic requiring explicit looping, traditional functions are preferable.

---

## Q2: Data Access

**Question:**  
You have been provided with a dataset containing daily weather observations. Each record includes the date, average temperature (in Celsius), precipitation (in mm), and wind speed (in km/h). Your task is to analyze this data using Python, focusing on data manipulation, functional programming, and lambda expressions.

**Sample Dataset:**

```python
data = [
    {"date": "2023-01-01", "temperature": 22, "precipitation": 0, "wind_speed": 10},
    {"date": "2023-01-02", "temperature": 18, "precipitation": 12, "wind_speed": 5},
    {"date": "2023-01-03", "temperature": 10, "precipitation": 0, "wind_speed": 20},
    {"date": "2023-01-04", "temperature": 15, "precipitation": 5, "wind_speed": 15},
    {"date": "2023-01-05", "temperature": 25, "precipitation": 0, "wind_speed": 8},
    # Add more entries as needed
]
```

**Question:**  
Print the temperature and wind speed recorded on "2023-01-03".

**Answer:**  
```python
day = [x for x in data if x["date"] == "2023-01-03"]
print("The temperature is {:.0f} and the wind speed is {:.0f}".format(day[0]["temperature"], day[0]["wind_speed"]))
```

---

## Q3: Simple Calculations

**Question:**  
Calculate and print the average temperature from the dataset.

**Answer:**  
```python
total = reduce(lambda acc, x: x["temperature"] + acc, data, 0)
avg = total / len(data)
print("The average temperature is", avg)
```

---

## Q4: Using Lambda and `map()`

**Question:**  
Using a lambda function with the `map()` function, create and print a list of temperatures converted from Celsius to Fahrenheit using the formula \( F = C \times 1.8 + 32 \).

**Answer:**  
```python
tempF = list(map(lambda x: x["temperature"] * 1.8 + 32, data))
print(tempF)
```

---

## Q5: Filtering Data with `filter()`

**Question:**  
Use a lambda function and `filter()` to extract days with no precipitation. Print the resulting list of dates.

**Answer:**  
```python
noP = list(filter(lambda x: x["precipitation"] == 0, data))
dates = list(map(lambda x: x["date"], noP))
print(dates)
```

---

## Q6: Advanced Data Aggregation with `reduce()`

**Question:**  
Using `reduce()` from the `functools` module and a lambda function, compute and print the total amount of precipitation over the dataset.

**Answer:**  
```python
total_p = reduce(lambda acc, x: acc + x["precipitation"], data, 0)
print("The total precipitation is", total_p)
```
```
