# Study Notes

## 1. What is SVD (Singular Value Decomposition)?

### Explanation:
- SVD is a mathematical technique used to decompose a matrix into three simpler matrices.
- It helps to analyze and manipulate data by breaking down complex structures.
- SVD is used widely in data science, machine learning, signal processing, and more.

### The Three Components:
1. **U (Left Singular Matrix):**
   - Represents patterns among the rows.
   - Orthogonal matrix containing the left singular vectors.
   
2. **S (Singular Values):**
   - Diagonal matrix containing singular values arranged in descending order.
   - Indicates the importance of each corresponding pattern.
   
3. **V^T (Right Singular Matrix):**
   - Represents patterns among the columns.
   - Orthogonal matrix containing the right singular vectors.

### Decomposition Formula:
\[
A = U \cdot S \cdot V^T
\]

### Uses of SVD:
1. **Dimensionality Reduction:** Reduces the number of features by keeping the most significant components.
2. **Image Compression:** Approximates the original matrix with fewer components to reduce file size while maintaining quality.
3. **Recommender Systems:** Identifies patterns in user preferences for making recommendations.
4. **Solving Linear Systems:** Used in solving systems of linear equations, especially in non-square or inconsistent systems.

---

## 2. How to Reconstruct a Matrix Using SVD?

### Steps:
1. **Perform SVD:** Obtain matrices \( U \), \( S \), and \( V^T \).
2. **Select Top \( k \) Components:** Choose the top \( k \) singular values and corresponding columns/rows of \( U \) and \( V^T \).
3. **Reconstruct the Matrix:**
   \[
   A_{approx} = U_{top} \cdot S_{top} \cdot V_{top}^T
   \]
   - \( U_{top} \) and \( V_{top}^T \) are reduced matrices.
   - \( S_{top} \) is a diagonal matrix with the top \( k \) singular values.

### Example:
- \( U_{top2} \) is \( m \times 2 \), \( S_{top2} \) is \( 2 \times 2 \), and \( V_{top2}^T \) is \( 2 \times n \).
- Multiplying \( U_{top2} \cdot S_{top2} \cdot V_{top2}^T \) gives an \( m \times n \) approximation of the original matrix.

---

## 3. Explain SVD in Simple Terms

### Simple Explanation:
- Think of a matrix as a grid of numbers representing data (e.g., an image or dataset).
- SVD breaks it down into three simpler components that capture patterns and structure in the data.
- The three components (\( U \), \( S \), \( V^T \)) represent different features of the original data:
   - \( U \): Row-wise patterns.
   - \( S \): Importance of patterns (singular values).
   - \( V^T \): Column-wise patterns.

### Why It Works:
- The singular values in \( S \) indicate how much information is captured by each pattern.
- By keeping only the largest singular values and corresponding vectors, the most important features are retained.

---

## 4. Example Use Case to Demonstrate the Components of SVD

### Use Case: Image Compression
- **Original Image:** A grayscale image is represented as a matrix where each element is a pixel intensity (0-255).
- **Perform SVD:** Decompose the matrix \( A \) into \( U \), \( S \), and \( V^T \).
- **Interpret Components:**
   - \( U \): Patterns in pixel intensities across rows.
   - \( S \): Importance of each pattern (singular values).
   - \( V^T \): Patterns in pixel intensities across columns.
- **Compress the Image:** Keep only the top \( k \) components to reduce data size while preserving the most significant patterns.
- **Reconstruction:** Multiply the reduced matrices to approximate the original image.

---

## 5. What is the Difference Between `df.mean()` and `np.mean()`?

### Differences:
1. **Data Structures Supported:**
   - `df.mean()`: Works with Pandas DataFrames and Series.
   - `np.mean()`: Works with NumPy arrays.
   
2. **Axis Parameter Differences:**
   - `df.mean(axis=0)`: Mean across columns (default).
   - `np.mean(arr, axis=0)`: Mean across rows for a 2D NumPy array.

3. **Handling Missing Values:**
   - `df.mean()`: Skips `NaN` values by default (`skipna=True`).
   - `np.mean()`: Returns `NaN` if the data contains `NaN`. Use `np.nanmean()` to skip `NaN`.

4. **Output Type:**
   - `df.mean()`: Returns a Pandas Series or scalar.
   - `np.mean()`: Returns a NumPy scalar or array.

5. **Performance:**
   - `np.mean()`: Faster for raw numerical operations.
   - `df.mean()`: Adds overhead due to handling labeled data and missing values.

---

## 6. Troubleshooting Matrix Reconstruction with SVD

### Issue: ValueError: Shapes Not Aligned
- Occurs when matrix dimensions do not match for multiplication.
- In SVD reconstruction, ensure:
   - \( U_{top2} \) is \( m \times 2 \).
   - \( S_{top2} \) is a \( 2 \times 2 \) diagonal matrix.
   - \( V_{top2}^T \) is \( 2 \times n \).

### Corrected Approach:
1. Convert \( S_{top2} \) to a diagonal matrix.
2. Multiply in the order: \( U_{top2} \cdot S_{top2} \cdot V_{top2}^T \).

---

## 7. Example: Correctly Using Matrix Slicing for SVD

### Code:
```python
# Take only the first 2 columns of U and the first 2 rows of Vt
U_top2 = U[:, :2]   # Selects all rows and first 2 columns
Vt_top2 = Vt[:2, :] # Selects first 2 rows and all columns
