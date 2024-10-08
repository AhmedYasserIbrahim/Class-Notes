## NumPy Basics

### Importing Libraries
```python
import numpy as np
import spacy  # Used for embedding
```

### Creating Arrays
```python
a = np.array([1, 2, 3, 4, 5])  # Define a NumPy array
s = np.array(5)                 # Define a scalar
```
- **Note**: NumPy arrays are favored over Python lists because they are optimized for speed and numerical operations. They allow for element-wise operations, which are more efficient than loops.

### Array Dimensions
```python
twoD_array = np.array([[1, 2, 3], [4, 5, 6]])
dimensions = twoD_array.shape    # Returns the dimensions of a NumPy array
```
- The `shape` attribute provides the dimensions of the array as a tuple, indicating the number of rows and columns.

### Vectors in Data Science
- A vector is a mathematical object that has both a magnitude and direction. In n-dimensional space, a vector can be represented as an ordered list of n numbers.
- Vectors are fundamental in data science as they represent features of data points. For instance, in a dataset of houses, each house can be represented as a vector where each dimension corresponds to a feature (like size, number of bedrooms, etc.).

### Vector Operations
```python
v = np.array([5, 8, 2])
w = np.array([3, 2, 7])
add = v + w                    # Performs vector addition
triple_size = 3 * v            # Scalar by vector multiplication
```
- Vector addition combines two vectors by adding their corresponding elements. Scalar multiplication scales a vector by a constant, changing its magnitude but not its direction.

### Dot Product
```python
dot_product = np.dot(v, w)     # Calculates the dot product between the two vectors
```
- The dot product of two vectors results in a scalar value that reflects how aligned the two vectors are. If the dot product is positive, the vectors point in a similar direction; if negative, they point in opposite directions; and if zero, they are orthogonal.

### Projection and Similarity
- The dot product can also be interpreted geometrically as a projection. It measures how much of one vector lies in the direction of another, providing insight into their similarity.
- The closer the vectors are in terms of direction, the higher the dot product, indicating greater similarity.

## Embeddings and Similarity

### Using SpaCy for Embeddings
```python
nlp = spacy.load("en_core_web_sm")  # Load the embedding model
a = 'apple'
b = 'banana'
e1 = nlp(a).vector                   # Embed the token 'apple'
e2 = nlp(b).vector                   # Embed the token 'banana'
dp = np.dot(e1, e2)                 # Get the dot product for similarity
print(dp)
```
- Word embeddings convert words into numerical vectors that capture semantic meaning. The dot product of these embeddings indicates the similarity between words: higher values suggest closer meanings.

### Vector Normalization
- Normalization is a crucial step in processing vectors. It helps maintain numerical stability and allows for meaningful comparisons between vectors of different magnitudes.
```python
norm_v = np.linalg.norm(v)            # Find the norm of vector v
norm_w = np.linalg.norm(w)            # Find the norm of vector w
normalized_v = v / norm_v              # Normalize vector v by dividing by its norm
normalized_w = w / norm_w              # Normalize vector w
```
- **Methods of Normalization**:
  - **Euclidean Norm**: The most common method, calculated as the square root of the sum of the squares of the vector components.
  - **Manhattan Norm** (L1 norm): The sum of absolute values of the components, useful in certain applications where you want to avoid squaring.
  - Normalization helps in reducing bias introduced by vector magnitude when comparing angles or directions.

### Cosine Similarity
- Cosine similarity is a metric used to measure how similar two vectors are, regardless of their magnitude. It is defined as the cosine of the angle between two vectors.
- Using cosine similarity, we can compare the direction of vectors to assess similarity, making it particularly useful in high-dimensional spaces like text data.

## Matrices and Linear Algebra

### Matrix Operations
- Matrices are two-dimensional arrays that represent a collection of numbers arranged in rows and columns. They are fundamental in linear algebra.
```python
matrix = np.array([[2, 4, 1], [8, 6, 2], [0, 0, 1]])
det = np.linalg.det(matrix)          # Compute the determinant
```
- Matrix operations such as addition, multiplication, and inversion are essential for many applications in data science, including transformations and linear systems.

### Inversion and Pseudo Inversion
- The inverse of a matrix \( A \) is another matrix \( A^{-1} \) such that \( A A^{-1} = I \), where \( I \) is the identity matrix.
```python
isInvertible = det != 0
rank = np.linalg.matrix_rank(matrix)  # Compute the rank
if isInvertible:
    inverse = np.linalg.inv(matrix)   # Compute the inverse
```
- A matrix is invertible if its determinant is non-zero. The rank indicates the number of linearly independent rows or columns, which affects invertibility.

### Pseudo Inverse
- For matrices that are not invertible, the pseudo inverse provides a way to find a solution to linear equations that may not have a unique solution.
```python
a = np.array([[2, 4], [1, 3], [0, 0]])
pseudo_inv = np.linalg.pinv(a)        # Compute the pseudo inverse
```
- The pseudo inverse minimizes the least squares error and can be used in regression analysis.

### Solving Linear Systems
```python
A = np.array([[2, -1, 3], [4, 2, 0], [5, -2, 4]])
b = np.array([3, 2, 1])
x = np.linalg.solve(A, b)             # Compute the solution of Ax = b using Gaussian elimination
```
- Solving linear systems is a common application in various fields, including physics, engineering, and economics. Techniques like Gaussian elimination are used to find solutions efficiently.

### Eigenvalues and Eigenvectors
```python
A = np.array([[4, 1], [1, 4]])
eigenvalues, eigenvectors = np.linalg.eig(A)  # Calculate eigenvalues and eigenvectors
```
- Eigenvalues and eigenvectors are fundamental in understanding linear transformations. An eigenvector of a matrix is a vector whose direction remains unchanged when the matrix is applied to it, while the eigenvalue indicates how much the eigenvector is stretched or compressed.

### Properties of Eigenvalues
- The trace of a matrix (sum of diagonal elements) equals the sum of its eigenvalues, and the determinant equals the product of its eigenvalues. These properties are useful in analyzing matrix behavior.

### Covariance
- Covariance measures how much two random variables vary together. A positive covariance indicates that as one variable increases, the other tends to increase, while a negative covariance indicates the opposite.
- Understanding covariance is crucial for various statistical methods, including Principal Component Analysis (PCA), which reduces dimensionality by identifying the directions (principal components) that maximize variance.

## Data Science Steps for PCA
1. **Normalization**: Standardize the data to have a mean of zero and a standard deviation of one.
2. **Covariance Matrix**: Create a covariance matrix between the variables to identify dependencies among them.
3. **Dimensionality Reduction**: Select the most significant eigenvectors, which correspond to the largest eigenvalues, to reduce dimensions while preserving variance.
4. **Projection**: Project the standardized data onto the selected dominant eigenvectors.

- The outcome is a transformed representation of the original data in a new space that retains the most important features, facilitating further analysis and interpretation.

## Conclusion
- **Encoding vs. Embedding**: Encoding assigns fixed values to categories, while embedding allows for a learned representation that captures deeper relationships.
- Applications of these concepts include predicting prices (e.g., housing) using linear regression, which models the relationship between variables under the assumption of linearity.

```

This version includes additional theoretical explanations for key topics, enhancing your notes for better understanding. If there are any specific areas you want to dive deeper into or further clarify, feel free to ask!
