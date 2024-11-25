# Introduction to Classification and Logistic Regression

## 1. Introduction to Classification

Classification is a supervised learning technique used to categorize data into predefined labels or classes based on their attributes. It helps in predictive analysis by assigning new data points to one of the known categories.

## 2. Logistic Regression for Binary Classification

Logistic regression is a statistical method used for binary classification tasks, where the goal is to predict one of two possible outcomes (e.g., yes/no, true/false). It models the probability of a certain class or event existing by using a linear combination of input features.

In logistic regression, the output is transformed using the logistic function (also known as the sigmoid function) to produce a probability value between 0 and 1.

## 3. Encoding Categorical Variables

Before feeding data into a machine learning model, categorical variables need to be converted into a numerical format. This process is known as **encoding**.

### 3.1 Simple Encoding

An example of simple encoding is converting "yes"/"no" values to 1/0:

```python
df['target'] = df['target'].map({'yes': 1, 'no': 0})
```

### 3.2 One-Hot Encoding

One-hot encoding converts categorical variables into a binary representation. Each category is transformed into a new column, and a 1 or 0 indicates the presence or absence of that category. It often provides better results than simple encoding, especially when dealing with nominal categories.

```python
# Using pandas get_dummies function
df_encoded = pd.get_dummies(df, columns=['category_column'])
```

## 4. Logistic Function (Sigmoid) and Logit

### 4.1 Logistic Function (Sigmoid)

The logistic function, or sigmoid function, transforms any real-valued number into a value between 0 and 1. It's defined by the equation:

\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]

- \( \sigma(z) \): Output between 0 and 1.
- \( z \): Input value (usually a linear combination of features).

The sigmoid function outputs the probability of a data point belonging to a particular class.

### 4.2 Logit Function

The logit function is the inverse of the sigmoid function. It maps probabilities back to the input space, allowing us to model the relationship between the features and the probability of a certain outcome.

\[
\text{logit}(p) = \ln\left(\frac{p}{1 - p}\right)
\]

- \( p \): Probability between 0 and 1.

The sigmoid and logit functions are inverses of each other, neutralizing one another in equations.

## 5. Loss Functions in Logistic Regression

To build and train a logistic regression model, we need a loss function that measures the discrepancy between predicted values and actual values.

### 5.1 Why Not Mean Squared Error (MSE)?

Mean Squared Error (MSE) isn't ideal for binary classification because it doesn't handle binary outcomes effectively and can lead to non-convex optimization problems.

### 5.2 Log Loss (Cross-Entropy Loss)

Log Loss, also known as Cross-Entropy Loss, is used to evaluate the performance of a classification model where the output is a probability value between 0 and 1.

\[
\text{Log Loss} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right]
\]

- \( N \): Number of samples.
- \( y_i \): Actual label (0 or 1).
- \( p_i \): Predicted probability.

By minimizing Log Loss, we adjust the model's weights to improve accuracy.

## 6. Encoding Numerical Values

Encoding isn't limited to categorical variables; sometimes numerical values are encoded to improve classification accuracy. Techniques like binning or scaling can help the model interpret numerical data more effectively.

## 7. Data Splitting: Train-Test Split

Splitting data into training and testing sets is essential for evaluating a model's performance on unseen data.

```python
from sklearn.model_selection import train_test_split

# X: features, y: target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

- **Training Set**: Used to train the model.
- **Testing Set**: Used to assess model performance.

This helps prevent overfitting and ensures that the model generalizes well to new data.

## 8. Confusion Matrix and Classification Metrics

### 8.1 Confusion Matrix

The confusion matrix is a table used to evaluate the performance of a classification model by comparing the actual values with the predicted values. It consists of four types of classifications:

- **True Positive (TP)**: Correctly predicted positive cases.
- **True Negative (TN)**: Correctly predicted negative cases.
- **False Positive (FP)**: Incorrectly predicted positive cases (Type I error).
- **False Negative (FN)**: Incorrectly predicted negative cases (Type II error).

The confusion matrix looks like this:

|                     | **Predicted Positive** | **Predicted Negative** |
|---------------------|------------------------|------------------------|
| **Actual Positive** | True Positive (TP)     | False Negative (FN)    |
| **Actual Negative** | False Positive (FP)    | True Negative (TN)     |

### 8.2 Classification Metrics

#### 8.2.1 Accuracy

Accuracy measures the overall performance of the model. It is the ratio of correctly predicted observations to the total observations.

\[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
\]

- **Interpretation**: High accuracy means the model is performing well on both positive and negative classes.

#### 8.2.2 Precision

Precision measures the model's ability to correctly predict positive observations. It is the ratio of true positive predictions to the total predicted positive observations.

\[
\text{Precision} = \frac{TP}{TP + FP}
\]

- **Interpretation**: High precision indicates a low false positive rate.

#### 8.2.3 Recall (Sensitivity)

Recall, also known as sensitivity or true positive rate, measures the model's ability to find all the relevant cases within a dataset.

\[
\text{Recall} = \frac{TP}{TP + FN}
\]

- **Interpretation**: High recall indicates a low false negative rate.

#### 8.2.4 F1 Score

The F1 Score is the harmonic mean of precision and recall, providing a balance between the two.

\[
\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
\]

- **Interpretation**: Useful when you need a balance between precision and recall.

#### 8.2.5 Specificity

Specificity measures the proportion of actual negatives that are correctly identified.

\[
\text{Specificity} = \frac{TN}{TN + FP}
\]

- **Interpretation**: High specificity indicates a low false positive rate for the negative class.

### 8.3 Summary of Metrics

- **Accuracy**: Overall correctness of the model.
- **Precision**: Quality of positive predictions.
- **Recall**: Ability to find all positive instances.
- **F1 Score**: Balance between precision and recall.
- **Specificity**: Correctness of negative predictions.

These metrics help in understanding different aspects of model performance and are crucial for selecting the right model for your specific use case.

---

By understanding and utilizing these concepts, you can build effective classification models and evaluate their performance accurately.
