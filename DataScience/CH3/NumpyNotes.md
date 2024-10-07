# NumPy Notes

## Introduction to NumPy
NumPy is a powerful library in Python for numerical computing. It provides support for arrays, matrices, and many mathematical functions to operate on these data structures.

### Why Use NumPy?
- **Performance**: NumPy arrays are optimized for speed and numerical operations compared to Python lists.
- **Ease of Use**: Operations on arrays are intuitive and require less code.

## Basic Array Operations

### Creating Arrays
```python
import numpy as np

# Define a 1D NumPy array
a = np.array([1, 2, 3, 4, 5])

# Define a scalar (optimized for performance)
s = np.array(5)

# Define a 2D NumPy array
twoD_array = np.array([[1, 2, 3], [4, 5, 6]])
```

### Array Properties
```python
# Get the shape of the array
shape = twoD_array.shape  # Returns the dimensions of the array
```

## Vectors and Their Operations
Vectors are essential in data science as they represent features in a dataset. 

### Vector Operations
```python
v = np.array([5, 8, 2])
w = np.array([3, 2, 7])

# Vector addition
add = v + w

# Scalar multiplication
triple_size = 3 * v

# Dot product
dot_product = np.dot(v, w)
```

### Practical Application: Similarity Measures
Vectors can represent embeddings in natural language processing (NLP).
```python
import spacy

nlp = spacy.load("en_core_web_sm")
a = 'apple'
b = 'banana'
e1 = nlp(a).vector  # Embed the token to a vector
e2 = nlp(b).vector

# Calculate similarity using dot product
dp = np.dot(e1, e2)
print(dp)
```

## Normalization and Stability
Normalization helps in stabilizing numerical values, especially in machine learning models.

### Methods of Normalization
```python
# Calculate the norm of a vector
norm_v = np.linalg.norm(v)

# Normalize the vector
normalized_v = v / norm_v
```

### Cosine Similarity
Cosine similarity measures the similarity based on the angular difference between vectors.
- **Semantic Search**: Uses cosine similarity to find the closest results to a query.

## Matrices and Their Operations
Matrices are multidimensional arrays that can perform complex operations without explicit loops.

### Matrix Operations
```python
# Matrix multiplication
matrix = np.array([[2, 4, 1], [8, 6, 2], [0, 0, 1]])
det = np.linalg.det(matrix)  # Compute the determinant
rank = np.linalg.matrix_rank(matrix)  # Compute the rank

if det != 0:
    inverse = np.linalg.inv(matrix)  # Inverse of the matrix
```

### Solving Linear Systems
You can solve linear equations using NumPy’s built-in functions.
```python
A = np.array([[2, -1, 3], [4, 2, 0], [5, -2, 4]])
b = np.array([3, 2, 1])
x = np.linalg.solve(A, b)  # Solve for x
```

## Eigenvalues and Eigenvectors
Understanding eigenvalues and eigenvectors is crucial in various applications, including Principal Component Analysis (PCA).

### Calculating Eigenvalues and Eigenvectors
```python
A = np.array([[4, 1], [1, 4]])
eigenvalues, eigenvectors = np.linalg.eig(A)
```

### Properties
- **Trace**: The sum of the diagonal elements, equal to the sum of eigenvalues.
- **Determinant**: The product of eigenvalues; a non-zero determinant indicates a non-singular matrix.
