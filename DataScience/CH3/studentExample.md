# Data Analysis with Pandas

## Importing Libraries

```python
import pandas as pd
import csv
import matplotlib.pyplot as plt
```

## Creating a DataFrame

### Sample Data

```python
data = {
    "Name": ["Ahmed", "Ali", "Baraa", "Hani", "Osama"],
    "Age": [16, 42, 33, 19, 27],
    "GPA": [3.2, 4.0, 1.9, 2.4, 2.8]
}
df = pd.DataFrame(data)  # Convert the dictionary to a DataFrame, a 2D array format that represents data in rows and columns
```

### Accessing Data

- **Accessing a Column**:
    ```python
    names = df["Name"]  # Access a column in the DataFrame
    ```

- **Getting the First Row**:
    ```python
    first = df.iloc[0]  # Get the first row in the data. Used with indexes
    ```

- **Accessing Specific Data by Label**:
    ```python
    first_GPA = df.loc[1, ["GPA"]]  # Used to access data by the label assigned, not necessarily the index.
    ```

- **Filtering Data**:
    ```python
    eligible = df.loc[df["Age"] > 18]  # loc can also be used to filter data in one line 
    ```

## Working with CSV Files

### Sample CSV Data

You can create a CSV file named `students.csv` with the following content:

```
Name,Age,GPA,Exam 1,Exam 2,Final
Ahmed,16,3.2,85,78,90
Ali,42,4.0,90,92,95
Baraa,33,1.9,60,70,65
Hani,19,2.4,75,80,78
Osama,27,2.8,80,75,77
Maya,22,3.5,88,85,90
Zara,25,3.9,92,94,93
Khaled,30,2.1,65,68,66
Lina,18,3.8,95,98,97
Omar,24,2.7,78,72,75
```

### Reading CSV Data

```python
location = r'C:\Users\yasse\Desktop\CS316\Python Practice\CH3\students.csv'  # Specify the path to the CSV file
students = pd.read_csv(location)
std_data = pd.DataFrame(students)  # Convert the data to a 2D DataFrame
```

### Data Cleaning and Analysis

- **Removing Duplicates**:
    ```python
    std_data.drop_duplicates(inplace=True)  # Remove any duplicates in the data
    ```

- **Counting Duplicates**:
    ```python
    numberOfDupes = std_data.duplicated().sum()  # Get the number of duplicates
    ```

- **Describing Data**:
    ```python
    top5 = std_data.head(5).describe()  # Statistical description of first 5 elements in data
    ```

- **Correlation Analysis**:
    ```python
    correlation = std_data[["Exam 1", "Exam 2", "GPA", "Final"]].corr()  # Create a correlational statistic of columns in the data
    ```

- **Grouping Data by Age**:
    ```python
    byAge = std_data.groupby("Age")["GPA"].mean()  # Used to create a smaller DataFrame of elements that have the same key value and find the average GPA for every group
    ```

## Data Visualization

- **Plotting Age**:
    ```python
    std_data["Age"].plot()  # Create a graph of index vs age
    ```

- **Creating a Scatter Plot**:
    ```python
    plt.scatter(std_data["Age"], std_data["GPA"])  # Create a scatter plot of age vs GPA
    plt.show()  # Display the graph
    ```
```

### Summary

This Markdown file provides a comprehensive overview of your data analysis workflow, including the necessary CSV data for use in your analysis. You can save this content as a `.md` file along with the `students.csv` file for easy reference and execution.
