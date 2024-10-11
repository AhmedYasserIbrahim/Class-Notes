# Pandas Study Notes

## Introduction to Pandas
Pandas is a powerful library in Python used for data manipulation and analysis. It provides two key data structures:
- **Series**: A one-dimensional array.
- **DataFrame**: A two-dimensional, table-like data structure.

---

## Pandas Series

### Create a Series
```python
import pandas as pd

nums = pd.Series([0, 1, 2, 3, 4, 5, 6])
evens = nums[0:6:2]  # Even numbers
odds = nums[1:5:2]   # Odd numbers
```

### Convert List to Pandas Series
```python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_to_series = pd.Series(arr)
```

### Series with Custom Index
```python
charIndexes = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(charIndexes['a':'d'])  # Inclusive slicing
```

### Convert Dictionary to Series
```python
dictionary = {"Name": "Ahmed", "Age": 19}
dict_to_series = pd.Series(dictionary)
print(dict_to_series)
```

---

## Pandas DataFrame

### Creating a DataFrame
```python
df = pd.DataFrame({
    "Name": ["Ahmed", "Ali", "Omar", "Baraa", "Saad", "Nora"],
    "Age": [19, 32, 13, 50, 33, 28],
    "GPA": [4.0, 2.8, 3.6, 1.5, 2.2, 3.9]
})
```

### Selecting Data from DataFrame
```python
names = df.loc[:, 'Name']  # Select all entries in the "Name" column
std1 = df.iloc[0]  # Retrieve the first row (first student's data)
tops = df.loc[df['GPA'] > 3]  # Filter rows with GPA greater than 3
```

### Handling Missing Data
```python
Null_values = df.isnull()  # Check for missing values
total_nulls = df.isnull().sum()  # Count total null values per column

df["GPA"].fillna(0, inplace=True)  # Fill missing GPA values with 0
df["Age"].fillna(df["Age"].mean(), inplace=True)  # Fill missing Age with mean
df.dropna(inplace=True)  # Remove rows with any missing data
df.dropna(subset=["Name"], inplace=True)  # Remove rows where "Name" is missing
df.dropna(axis=1, inplace=True)  # Remove columns with missing data
```

### Data Manipulation
```python
df["ID"] = df["Name"] + "_" + df["Age"].astype(str)  # Create new column by concatenating Name and Age
df.drop(columns=["ID"], inplace=True)  # Remove the "ID" column
df.rename(columns={"GPA": "gpa"}, inplace=True)  # Rename the "GPA" column to "gpa"
df["DoubleGPA"] = df["gpa"].apply(lambda x: x * 2)  # Create new column by applying a function
df["Name"] = df["Name"].map(lambda x: "NaN" if pd.isnull(x) else x)  # Map null values to "NaN" in the "Name" column
```

### Sorting and Ranking Data
```python
df.sort_values(by="Name", ascending=True)  # Sort by "Name" in ascending order
ranking = df["gpa"].rank()  # Rank students by GPA
```

### Grouping and Aggregating Data
```python
Same_name = df.groupby("Name")  # Group by "Name"
GPA_per_name = df.groupby("Name")["gpa"].agg('mean')  # Calculate average GPA per name
```

---

## Advanced DataFrame Operations

### Creating a New DataFrame
```python
data = {
    'number': [1, 2, 3, 4, 5],
    'student_id': ['120060257', '211110888', '211210095', '212110756', '212110889'],
    'gender': ['male', 'female', 'male', 'female', 'male'],
    'major01': [0.25, 15.22, 13.25, 5.91, 11.00],
    'major02': [0.00, 10.75, 15.43, 1.25, 13.00],
    'project': [0.00, 14.67, 16.25, 5.00, 6.67],
    'final': [13.0, 27.0, 25.0, 7.0, 27.0],
    'term': ['fall', 'fall', 'fall', 'fall', 'fall'],
    'year': [2015, 2015, 2015, 2015, 2015]
}

stds = pd.DataFrame(data)
stds.info()  # Get summary of the DataFrame
stds.describe()  # Summary statistics
```

### Finding Maximum and Counting Unique Values
```python
stds["final"].max()  # Maximum value in "final" column
stds["gender"].value_counts()  # Count occurrences of each gender
stds["gender"].value_counts(normalize=True)  # Normalize the value counts (get percentage)
```

### Correlation Matrix
```python
stds[["major01", "major02", "final"]].corr()  # Correlation matrix
```

---

## Data Visualization

### Plotting Data with Matplotlib
```python
import matplotlib.pyplot as plt

stds["final"].plot(title="Final Grades")  # Line plot of final grades
plt.show()  # Display the plot

stds["major01"].plot.scatter(x=stds["major01"], y=stds["major02"])  # Scatter plot
```

---

## Working with Time Data

### Dealing with Time Data
```python
df["date"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour"]])  # Convert columns to datetime
df.resample('D').mean()  # Resample the data by day and calculate the mean

df["temperature"].rolling(window=24).mean()  # Rolling mean of temperature over 24 hours
```

---

With this, you'll have a comprehensive Pandas study guide. You can refer to the examples and explanations to reinforce your understanding of the concepts and functions.
