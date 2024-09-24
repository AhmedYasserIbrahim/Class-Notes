## Q1: Python's Built-in Data Structures

### Characteristics

- **Lists**: Mutable, ordered, indexed, allow duplicates, and can store different data types.
- **Tuples**: Immutable, ordered, indexed, allow duplicates, and can store different data types.
- **Sets**: Mutable, unordered, unindexed, and do not allow duplicates.
- **Dictionaries**: Mutable, ordered (Python 3.7 and later), keys are immutable, and accessible by keys.

### Performance Considerations

The choice of data structure significantly impacts performance:

- **Lists**: Versatile, but slow for insertion, deletion, and access (O(n) for insertion/deletion).
- **Tuples**: More efficient than lists due to immutability (O(1) for access).
- **Sets**: Fast for insertion, deletion, and access due to hashing (average O(1)).
- **Dictionaries**: Efficient for key lookups (average O(1)).

### Appropriate Usage

- **Lists**: Use for mutable records, such as a list of names.
- **Tuples**: Use for immutable records or as keys in a dictionary, such as coordinates.
- **Sets**: Use for eliminating duplicates and efficient membership checking, such as unique user IDs.
- **Dictionaries**: Use for key-value pairs, such as mapping product IDs to product names.

---

## Q2: Context: Sales Data Analysis

**Dataset Example:**

```python
sales_data = [
    {'product': 'smartphone', 'quantity': 10, 'revenue': 7000},
    {'product': 'laptop', 'quantity': 5, 'revenue': 5000},
    {'product': 'tablet', 'quantity': 20, 'revenue': 6000},
    {'product': 'smartphone', 'quantity': 15, 'revenue': 10500},
    {'product': 'laptop', 'quantity': 2, 'revenue': 2000},
    {'product': 'tablet', 'quantity': 5, 'revenue': 1500},
    {'product': 'accessory', 'quantity': 50, 'revenue': 1000}
]
```

### Question 1: Basic Data Retrieval

**Task:** Write a Python function named `total_sales()` that calculates the total revenue generated from all sales.

**Answer:**
```python
def total_sales():
    total = reduce(lambda acc, x: acc + x["revenue"], sales_data, 0)
    return total

print("The total revenue is", total_sales())
```

---

### Question 2: Product-based Revenue Calculation

**Task:** Write a Python function named `revenue_by_product()` that calculates the total revenue generated for each type of product.

**Answer:**
```python
def revenue_by_product():
    done = []
    revs = {}
    for data in sales_data:
        if data["product"] in done:
            continue
        done.append(data["product"])
        perProduct = [x["revenue"] for x in sales_data if x["product"] == data["product"]]
        total = sum(perProduct)
        revs[data["product"]] = total
    return revs

print(revenue_by_product())
```

---

### Question 3: Filtering and Summing Specific Sales Data

**Task:** Write a Python function named `high_value_sales()` that finds and sums the revenues from sales of a specific product that exceed a given threshold.

**Answer:**
```python
def high_value_sales(name, threshold):
    perProduct = [x for x in sales_data if x["product"] == name and x["revenue"] > threshold]  # List comprehension
    total = reduce(lambda acc, x: x["revenue"] + acc, perProduct, 0)  # Lambda function
    return total
```

---

### Question 4: Sorting and Analyzing Sales Data Using Tuples and Lambda Expressions

**Task:** Write a Python function named `top_selling_products()` that identifies the top three selling products based on quantity sold.

**Answer:**
```python
def quantity_by_product():
    done = []
    quants = []
    for data in sales_data:
        if data["product"] in done:
            continue
        done.append(data["product"])
        perProduct = [x["quantity"] for x in sales_data if x["product"] == data["product"]]
        total = sum(perProduct)
        quants.append((data["product"], total))  # Return a list of tuples
    return quants

def top_selling_products():
    sortByQuantity = sorted(quantity_by_product(), key=lambda x: x[1], reverse=True)  # Sort by quantity
    out = []
    for i in range(3):
        out.append(sortByQuantity[i])
    return out  # Return a list of tuples

print(top_selling_products())
```
```
