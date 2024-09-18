```markdown
# Pandas Overview

- **Pandas** is a library built on NumPy for data manipulation and analysis.
- It is useful for working with structured data to perform operations such as cleaning and transformation.
- **Scalable and flexible**, Pandas works well with both small and large datasets.
- It can load data from various formats, including JSON, SQL, and Excel.

## Key Components

- **Series**: A 1D indexed array that can store heterogeneous data and supports vectorization operations.
- **DataFrame**: A 2D array organized in rows and columns.

## Comparison with Other Tools

- **Excel**: Less powerful and efficient for larger datasets.
- **SQL**: Used for querying databases rather than data analysis, which complements Pandas.

## Basic Usage

```python
import pandas as pd  # Install via pip

# Creating a Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])  # Set indexes to characters
first = s['a']          # Get the first element in the Series
three = s['a':'c']      # Get the first three elements using slicing
evens = s[0:3:2]        # Get elements from index 0 to 3 with a step of 2
```

> Note: We cannot access an index using the value because a value can be duplicated.

## DataFrame Operations

- Use `pd.DataFrame` to convert a dictionary or an array into a DataFrame.
- Access a column using the column label: `df["Name"]`.
- Access a row using the index: `df.iloc[0]`.
- Use `df.loc[]` for accessing data based on row or column labels.
- Filter data with: `df.loc[df["Age"] > 25]`.
- Specify rows and columns with: `df.iloc[0:3, 1:3]`.
- Read data using: `pd.read_csv("data.csv")`.

## Example DataFrame Creation

```python
data = {"Name": ["Ahmed", "Ali"], "Age": [18, 26]}
df = pd.DataFrame(data)  # Convert your data to a DataFrame
```

## Additional Libraries

```python
import sqlite3            # For SQL queries
import psycopg2           # For PostgreSQL queries
import json               # For JSON files
```

## Loading Data

```python
location = r'C:\Users\yasse\Downloads\yourfile.csv'  # Specify the path as a raw string
df = pd.read_csv(location)                              # Load the dataset
print(df.head(5))                                      # Print the first few rows
df.info()                                              # Information about columns, rows, datatypes, and missing info
```

> We should assign values to NaNs during the data cleaning process.

### Data Cleaning

- Use `df.dropna(inplace=True)` to remove rows with missing data.
- Count duplicates: `duplicate_count = df.duplicated().sum()`.
- Remove duplicates: `df.drop_duplicates(inplace=True)`.
- Convert column data types: `IDs = df["University_ID"].astype("int32")`.

### Statistical Analysis

- Use `df.describe()` for a statistical description of the dataset.
- Compute correlations: `correlation = df[["GPA", "Mark"]].corr()`.
- Group data: 
  ```python
  df.groupby("university_level")["GPA"].mean()  # Average GPA by level
  df.groupby("university_level")["GPA"].describe()  # Descriptive stats
  ```

## Weather Analytics Use Case

- Use `pd.to_datetime` to convert time from a specified format to a timestamp.
- Check for null values: `df.isnull().sum()`.
- Get data types of columns: `df.dtypes`.
- Use `errors='coerce'` to convert non-numeric values to NaN.
- Plotting temperature data:
  
```python
import matplotlib.pyplot as plt  # For plotting
df["temperature"].plot()         # Plot the temperature column
```

- Resample data: `df.resample('D').mean()` to aggregate daily values.
- Use `.rolling(window=24).mean()` for overlapping windows, averaging 24 values.

--- 
```

This Markdown file summarizes your notes, providing a structured format for easy reading and understanding.
