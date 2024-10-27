# Data Science Theory Study Guide

## 1. What is the difference between covariance and correlation matrix?

- **Covariance Matrix**:
  - Measures how much two variables change together.
  - Values can range from negative to positive infinity.
  - Positive values indicate that both variables increase or decrease together, while negative values indicate an inverse relationship.

- **Correlation Matrix**:
  - Standardizes the values from the covariance matrix, scaling them between -1 and 1.
  - Measures the strength and direction of the linear relationship between variables.
  - A value of 1 indicates a perfect positive relationship, -1 a perfect negative relationship, and 0 no relationship.

In short, the covariance matrix shows the raw joint variability, while the correlation matrix normalizes this to provide a more interpretable measure of association.

## 2. When do we replace missing values with mean, median, or drop them?

- **Replace with Mean**:
  - Use when the data is **normally distributed** (i.e., symmetric without outliers).
  - The mean preserves the overall average and is suitable for continuous variables with relatively few missing values.

- **Replace with Median**:
  - Choose the median when the data is **skewed** or contains **outliers**, as it is more robust and less affected by extreme values.
  - Common for features like income, which can have large outliers.

- **Drop Missing Values**:
  - Drop rows or columns with missing values when the **proportion of missing data is high**, or when imputing could introduce bias.
  - Suitable if you have **enough data** and removing some entries won't significantly impact the analysis.

## 3. Does replacing with the median reduce variance?

Yes, **replacing missing values with the median reduces variance**. Since the median is a measure of central tendency, substituting missing values with a central value reduces the spread of data points around the mean, thereby decreasing variability. However, this may lead to a **loss of data variability** and may affect the model's performance if variance is an important feature.

## 4. Does replacing with the mean reduce variance?

Yes, **replacing missing values with the mean** also reduces variance, but typically to a lesser extent than using the median. This is because the mean is more sensitive to the actual distribution of the data, including outliers. While it still reduces the spread of data around the mean, it retains more of the original variability compared to the median.

## 5. Explain every component and what it represents in a box plot.

In a **box plot**, the components represent:

- **Median (Central Line)**:
  - Represents the **middle value** of the data, with half of the observations below and half above.

- **Interquartile Range (IQR) (Box)**:
  - Shows the **middle 50%** of the data, from the **first quartile (Q1)** to the **third quartile (Q3)**.
  - **Q1** is the 25th percentile, while **Q3** is the 75th percentile.

- **Whiskers**:
  - Extend from the box to the **minimum and maximum values** within **1.5 times the IQR**. Anything outside this range is considered an outlier.

- **Outliers (Individual Points)**:
  - Data points that fall **outside the whiskers** and indicate unusual or extreme values.

## 6. What is SVD? Explain the concept, use, components, reconstruction, and a real-world example.

### Concept
**Singular Value Decomposition (SVD)** is a matrix factorization technique that decomposes a matrix into three other matrices:
\[
A = U \Sigma V^T
\]
where:
- **U**: An m × m matrix of left singular vectors.
- **Σ (Sigma)**: An m × n diagonal matrix of singular values.
- **V^T**: The transpose of an n × n matrix of right singular vectors.

### Components
1. **U (Left Singular Vectors)**:
   - Represents the original data's features in a new orthogonal basis.

2. **Σ (Sigma) (Singular Values)**:
   - Diagonal matrix where values represent the amount of variance captured by each singular vector.

3. **V^T (Right Singular Vectors)**:
   - Represents the original data's samples in another orthogonal basis.

### Use Cases
1. **Dimensionality Reduction**: Reduces the number of dimensions while preserving essential features.
2. **Data Compression**: Uses fewer components to approximate the original matrix.
3. **Noise Reduction**: Removes small singular values associated with noise.
4. **Recommendation Systems**: Identifies latent factors in user-item interactions.

### Reconstruction
To reconstruct the original matrix:
\[
A \approx U_k \Sigma_k V_k^T
\]
where **k** is the number of largest singular values retained.

### Real-World Example: Image Compression
1. **Perform SVD**: Decompose the image matrix into **U**, **Σ**, and **V^T**.
2. **Reduce the Rank**: Keep the top **k** singular values.
3. **Reconstruct the Image**: Multiply **U_k**, **Σ_k**, and **V_k^T** to get an approximation.
4. **Component Demonstration**:
   - **U_k** represents primary patterns (e.g., edges).
   - **Σ_k** indicates pattern significance.
   - **V_k^T** describes how patterns form the original image.
