# NumPy Notes

## Introduction to NumPy
NumPy is a powerful library in Python for numerical computing. It enables efficient manipulation of large arrays and matrices, along with a collection of mathematical functions to operate on these data structures.

### Why Use NumPy?
- **Performance**: NumPy arrays are optimized for speed and provide efficient storage for large datasets.
- **Ease of Use**: Operations on arrays are intuitive and require less code compared to Python lists.

## Basic Array Operations

### Creating Arrays
NumPy allows you to create arrays in various dimensions.
```python
import numpy as np

# Define a 1D NumPy array
a = np.array([1, 2, 3, 4, 5])

# Define a scalar (optimized for performance)
s = np.array(5)

# Define a 2D NumPy array
twoD_array = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", a)
print("2D Array:\n", twoD_array)
```

### Array Properties
Understanding the properties of arrays is crucial for effective manipulation.
```python
# Get the shape of the array
shape = twoD_array.shape  # Returns the dimensions of the array
print("Shape of 2D Array:", shape)
```

## Vectors and Their Operations
Vectors are fundamental in data science, representing features in datasets.

### Definition of Vectors
A vector is an ordered array of numbers that expresses a point in n-dimensional space. In data science, vectors are used to represent features of data.

### Vector Operations
```python
v = np.array([5, 8, 2])
w = np.array([3, 2, 7])

# Vector addition
add = v + w  # Adds corresponding elements
print("Vector Addition:", add)

# Scalar multiplication
triple_size = 3 * v  # Scales vector by 3
print("Scalar Multiplication:", triple_size)

# Dot product
dot_product = np.dot(v, w)  # Computes the dot product
print("Dot Product:", dot_product)
```

### Practical Application: Similarity Measures
Vectors can represent embeddings in natural language processing (NLP). The dot product can be used to measure similarity between word embeddings.
```python
import spacy

nlp = spacy.load("en_core_web_sm")
a = 'apple'
b = 'banana'
e1 = nlp(a).vector  # Embed the token to a vector
e2 = nlp(b).vector

# Calculate similarity using dot product
dp = np.dot(e1, e2)
print("Dot Product Similarity:", dp)
```

## Normalization and Stability
Normalization is crucial for stabilizing numerical values, especially in machine learning models.

### Methods of Normalization
Normalization can prevent numerical instability and improve model performance.
```python
# Calculate the norm of a vector
norm_v = np.linalg.norm(v)

# Normalize the vector
normalized_v = v / norm_v  # Ensures the vector has a magnitude of 1
print("Normalized Vector:", normalized_v)
```

### Cosine Similarity
Cosine similarity measures the similarity based solely on the angle between vectors, making it useful in semantic search.
```python
# Calculate cosine similarity
cosine_similarity = np.dot(normalized_v, normalized_v)  # Should be 1.0 for the same vector
print("Cosine Similarity:", cosine_similarity)
```

## Matrices and Their Operations
Matrices are two-dimensional arrays that can perform complex operations without explicit loops.

### Matrix Operations
```python
# Define a matrix
matrix = np.array([[2, 4, 1], [8, 6, 2], [0, 0, 1]])

# Compute properties of the matrix
det = np.linalg.det(matrix)  # Compute the determinant
rank = np.linalg.matrix_rank(matrix)  # Compute the rank
print("Determinant of Matrix:", det)
print("Rank of Matrix:", rank)

# Inversion of a matrix
if det != 0:
    inverse = np.linalg.inv(matrix)  # Inverse of the matrix
    print("Inverse of Matrix:\n", inverse)
else:
    print("Matrix is not invertible.")
```

### Solving Linear Systems
You can solve linear equations using NumPy’s built-in functions, which is essential in many applications such as predictive modeling.
```python
A = np.array([[2, -1, 3], [4, 2, 0], [5, -2, 4]])
b = np.array([3, 2, 1])
x = np.linalg.solve(A, b)  # Solve for x using Gaussian elimination
print("Solution of Linear System:", x)
```

## Eigenvalues and Eigenvectors
Eigenvalues and eigenvectors are crucial in understanding transformations in linear algebra.

### Calculating Eigenvalues and Eigenvectors
```python
A = np.array([[4, 1], [1, 4]])
eigenvalues, eigenvectors = np.linalg.eig(A)  # Compute eigenvalues and eigenvectors
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
```

### Properties of Eigenvalues
- **Trace**: The sum of the diagonal elements, equal to the sum of eigenvalues.
- **Determinant**: The product of eigenvalues; a non-zero determinant indicates a non-singular matrix.
