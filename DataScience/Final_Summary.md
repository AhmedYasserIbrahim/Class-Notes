# Final Summary for CS316 - Semester 242

Hello! This is Ahmed Yasser's final summary for CS316 in semester 242. Please feel free to use it and good luck!

---

## 1. Gradient Descent

Gradient descent is an optimization technique that is used to find the best solution to a problem. The technique starts by assuming a random point on the function graph and uses the slope at that point to determine how far we are from the optimal solution that has zero error and that would be the lowest point on the graph. The parameters are then modified to improve the model.

**Function:**

$$
x_{\text{new}} = x_{\text{old}} - \alpha \nabla f(x_{\text{old}})
$$

- The function modifies the parameters to make a new prediction for every iteration. \(x_{\text{new}}\) is the new value and \(x_{\text{old}}\) is the value for the iteration just done. 
- \(\alpha\) is the learning rate that tells us the size of the step for every time. Too large could result in overshooting and missing the minimum value, causing instability as the function might never converge to the optimal solution, and too small would take too much time to optimize.
- The function is the loss function and its derivative (gradient for multiple parameters) points to the slope, meaning how much the loss changes when we modify the predicted value. \(\nabla f(x_{\text{old}})\) is the slope of the current function at the predicted value. It points to the steepest ascent; hence the negative sign as we are aiming for the lowest slope.

Gradient descent is simple, easy to implement (only requires computing the gradient), and efficient as it points directly to the minimum. It provides the optimal solution in convex situations and in non-convex functions it still provides high accuracy. Used if there are no external constraints.

---

## 2A. Classification

Classification is used to categorize data based on predefined labels (discrete) rather than continuous data which uses regression to predict an actual value on a metric. It uses supervised learning in applications such as fraud detection and image recognition.

Classification has many techniques which include:

- **Logistic Regression**: Used in binary classification (can be adapted to multi-class classification using the one-vs-rest concept) to find the probability that an outcome belongs to a specific class or not. Then it provides a categorized output based on the set threshold.

Other techniques include:

- **Decision Trees**: Similar to flowcharts, there are categorized possible inputs and the flow shows where the output is expected to be.
- **Support Vector Machines**: Finds the hyperplane that splits the data into categories with the maximum margin between the line and values from both sides for robustness and avoiding overfitting.
- **Random Forest**: Combines decision trees to vote for a class for categorizing the data. Reduces overfitting and error.
- **Neural Networks**: Similar to the brain where layers of nodes learn through adjusting parameters or weights to converge and minimize loss.
- **K Nearest Neighbors (KNN)**: Finds the closest \(k\) points in the space and checks their categories. Based on the majority vote, the point would be categorized.

Encoding is often used when dealing with data types in classification to convert to a numerical format understood by the model.

---

2. Logistic Functions
Logistic functions convert any value into a probability between 0 and 1, commonly used in classification tasks such as logistic regression.

Sigmoid Function: The sigmoid function takes an input value z (often a linear combination of features and weights) and converts it to a probability between 0 and 1.

Sigmoid: sigma(z) = 1 / (1 + e^(-z))

This function outputs values between 0 and 1 and is shaped like the letter S.

Logit Function: The inverse of the sigmoid function, used to retrieve the original z value before it was converted into a 0–1 probability scale.

Softmax Function: A generalization of the sigmoid function for multi-class classification. For class j, it outputs a probability by taking the exponential of z_j and dividing it by the sum of exponentials of all z_i values.

Softmax for class j: P(class j) = e^(z_j) / (Σ e^(z_i))

This ensures that the probabilities of all classes sum up to 1.

3. Activation Functions
Activation functions introduce non-linearity into a neural network, allowing it to learn complex patterns. Without activation functions, a neural network would behave like a linear model, limiting its ability to capture complex relationships in data.

Types of Activation Functions
ReLU (Rectified Linear Unit):

ReLU(z) = max(0, z)

This function sets negative values to 0 and keeps positive values as they are. However, it can cause the "dead neuron problem" if neurons consistently produce negative values.

Tanh (Hyperbolic Tangent):

tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z))

Output is between -1 and 1. This function can handle balanced data more effectively than ReLU, but it still suffers from the vanishing gradient problem if z becomes very large or very small.

Leaky ReLU:

Leaky ReLU(z) = z if z ≥ 0, or α*z if z < 0 (where α is a small positive constant, like 0.01)
This variation of ReLU allows a small gradient to flow for negative values of z, preventing neurons from dying out completely.

---

## 4. Convex Functions and Optimization

Optimization improves the model's performance by reducing the error based on the loss function.

- **Constrained Optimization**: Includes a condition that limits the domain (e.g., budget limits).
- **Unconstrained Optimization**: Used in parameter optimization over the entire domain.

- A **convex function** is a function where the local minimum is also the global minimum. A line connecting any two points on the graph lies above or on the graph.
- **Convex Optimization** involves finding the minimum value of a convex function over a specified constraint (convex set). If the global minimum is outside the set, the closest minimum within the set is selected.

Convex optimization helps:
1. Formalize the problem.
2. Ensure solutions meet constraints.
3. Guarantee optimal solutions.
4. Select the best algorithm.

---

## 5. Mean Squared Error

MSE is a loss function that evaluates the accuracy of the model based on the difference between the actual and predicted values. The formula is the average of the summation of squared the difference between the expected and actual value for every point. Squaring ensures all values are positive and it penalizes larger errors more than smaller ones.

$$
L(\theta) = \frac{1}{n} \sum (y_i - \hat{y}_i)^2
$$

- \(L\) is the loss function (MSE in this case) and \(\theta\) is the set of predicted parameters or weights that we evaluate their accuracy in the regression analysis to evaluate the model.

Gradient descent is done for every parameter separately in the regression analysis function to optimize the contribution of every input feature independently on the performance of the model. The bias is not multiplied by any feature so it shifts the whole model.

---

## 6. Overfitting and Underfitting

Overfitting occurs when the model "memorizes" the training data or learns it too closely, meaning that it captures the noise and outliers not only the patterns. This means that the model is too complex and it would work well on training data but will not generalize to unseen data. The training loss would be too low and the testing loss would be high.

**Variance** is an error measure due to sensitivity to small fluctuations in the dataset, resulting in capturing noise and causing overfitting.

Underfitting means that the model is too simple, so it does not capture the underlying patterns of the data and its predictions would therefore be inaccurate. Both the training and testing data would be high. 

**Bias** is an error measure that oversimplifies complex real world problems by missing relevant features or making incorrect assumptions, resulting in underfitting.

The goal is to find a good balance tradeoff between bias and variance to achieve an accurate model that generalizes well to unseen data.

$$
\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error}
$$

Irreducible error is the inherent noise in the data that results from measurement errors or unpredictable factors. It cannot be removed regardless of how the model is designed.

A training curve can be graphed to plot the size of the training dataset versus the error percentage. If both the training and validation errors are high and do not decrease significantly as the training dataset size increases, it means that there is underfitting (high bias). If the training error is low but validation error is high then there is overfitting (high variance). The goal is to find the optimal tradeoff point with the best training and testing errors.

---

## 7. Regularization

Regularization is a technique that is used to add a penalty to the loss function to prevent overfitting. This penalty prevents the model from having high coefficients, which means relying too much on the complex patterns and noise in the data. Regularization has many types:

**a. L1 Regularization (Lasso):** Adds a penalty equal to the summation of the absolute value of the coefficients, which encourages the model to minimize the value of the coefficients as much as possible. Some of the coefficients would reach exactly zero which means that those features are unimportant.

**b. L2 Regularization (Ridge):** Adds a penalty equal to summation of square the coefficients, which means that coefficients of features would shrink towards zero to minimize the penalty, but features would not be exactly zero. This results in creating a robust and simpler model (avoid overfitting) but retaining all features.

**c. Elastic Net:** Combines the advantages of both regularization models by adding the L1 and L2 penalty together. L1 creates a sparse model that does feature selection. L2 creates a simpler and more robust model that retains all features.

$$
\text{Penalty} = \lambda \sum |w_i| + \lambda \sum (w_i)^2
$$

\(\lambda\) is the strength of the penalty.

---

## 8. Cross Validation

Cross validation is a method used to evaluate how well the model generalizes to unseen data. Instead of having a single train-test split, the data is divided to subsets to allow every point to be used for both training and testing. Then, the model selection is done based on the best model across the splits of the data. This helps build a better model that reduces overfitting and underfitting.

**a. K-Fold:** The data is split into k folds. In every iteration, k-1 folds are used for training and 1 fold is used for testing. The final performance is the average of the results across all splits. This ensures the efficient use for the data as every fold would be used once for testing, resulting in k iterations. It also reduces bias.

**b. Leave One Out (LOOCV):** A special type of k-fold where k=n, meaning that in every iteration, all data points would be used for training and only one data point would be used in testing, resulting in n iterations. It is computationally expensive and may be unstable because there is only one test point for every iteration. The advantage is that it maximizes the amount of data used in training and highlights the importance of every single data point.

---

## 9. Model Selection and Hyperparameter Tuning

Model selection means choosing the best way to build a model for a specific task (e.g., neural network or linear regression). Hyperparameter tuning means choosing the best values for the parameters that are not learned as the model is trained, but instead the parameters that control the training of the model itself (e.g., learning rate or regularization strength).

**a. Grid Search:** Tries the combinations of all the parameters to find the best combination. It guarantees finding the best solution but is computationally expensive. (Small Datasets)

**b. Random Search:** Tries randomly selected combinations of parameters from the parameter space and uses the best one. It is efficient but does not guarantee finding the best combination. (Large datasets and abundant resources but needs simplicity)

**c. Bayesian Optimization:** Uses probabilistic models to find the best hyperparameters by learning from previous evaluations. It iterates through the promising areas of the parameter space based on probabilities. It is best for efficiency but complex to implement. (Limited Resources and need efficiency)

---

---

## 10. Linear Regression

Linear regression is a statistical model that is used to predict a value of a target dependent variable based on a combination of the feature independent variables by finding the best fit linear equation.

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \epsilon
$$

- **y** is the target variable.
- **x** are the features.
- **\(\beta\)** are the weights (the importance of every feature and how much it affects the target variable). Training adjusts those weights to minimize the loss function.
- **\(\beta_0\)** is the intercept that represents the value of y when all features are 0. It is the baseline for the prediction without predictors.
- **\(\epsilon\)** is the error term that accounts for variability in y that cannot be explained using a linear model. It measures the difference between the predicted and actual values for y. It has a mean of 0 and a constant variance meaning that the error is random and consistent. Training reduces the value of \(\epsilon\) but it will never be zero.

### Assumptions when using a linear regression model:

1. **Linearity:** There is a linear relationship between the features and the target variable.
2. **Independence:** One observation of a feature should not affect another observation.
3. **Homoscedasticity:** The error term \(\epsilon\) is roughly the same regardless of the independent variables.
4. **Normality:** The error distribution is normal (bell-shaped) and the mean of errors is 0. Needed for statistical tests such as confidence intervals to work properly.

The method of least squares is a way to compute the best weights for a linear regression model by minimizing the MSE. This gives the best predictions for y.

---

## 11. Evaluation Metrics

Ordinary Least Squares (OLS) regression report involves analyzing statistics to evaluate the efficacy and relevance of the regression model. Common metrics for evaluation include:

- **MSE:** Mean Squared Error, measures the average of the squared differences between predicted and actual values.

- **RMSE:** Root Mean Squared Error, the square root of the MSE to provide the error in the same measurement as that of the dependent variable for easier interpretation.

- **Coefficients:** Intercept and weights in the equation for linear regression.

- **Standard Errors:** Indicate the accuracy of the coefficient values (should be minimized).

- **T statistics:** Ratio of the coefficient over its standard error. Shows if the predictor has a meaningful and significant effect on y or not (is it significantly different from 0).

- **P value:** Tests the significance of each coefficient. P value < 0.05 means the predictor is significant.

- **R squared:** Amount of variance in y explained by the independent variables. Closer value to 1 means better model fit and smaller error term value.

- **Adjusted R squared:** R squared but adjusted to the number of predictors. Penalizes having irrelevant predictors.

- **F statistic:** Tests the overall significance of the model. Checks if at least one predictor significantly affects y.

- **Durbin Watson Statistic:** Measures the autocorrelation or relationship between errors. Close to 2 means the errors are independent. Otherwise, the model would be missing patterns.

- **AIC and BIC:** Metrics for comparing models. Lower value indicates a better model fit based on performance and complexity.

**R squared** is used to measure how well the variance in y is explained by the dependent variables or basically how well the dependent variables can predict the value for y. Closer to 1 means that the model predicts the value of y well. Standard Error of Regression (SER) is basically the sum of errors or distances from the regression line. SER should be minimized for better models. Together, R squared and SER can measure how well the model fits the data. Residual analysis refers to analyzing the differences between actual and predicted values. Residual analysis is needed to check the assumptions made by linear model and verify them.

---

## 12. Classification

In classification, data is assigned into predefined categories by using supervised learning and relying on previous instances.

A confusion matrix is used to evaluate the performance of a classification model when we have the correct outputs (labels). It has four parts:

- **True Positives (TP):** Correctly predicted positive observations.
- **True Negatives (TN):** Correctly predicted negative observations.
- **False Positives (FP):** Incorrectly predicted as positive.
- **False Negatives (FN):** Incorrectly predicted as negative.

**Remark:** The second letter is always the prediction of the model. The first letter is whether the prediction is right or wrong.

By having the confusion matrix, we can generate the classification report to evaluate the accuracy of the classification model using the following metrics:

- **Accuracy:** The ratio of correctly predicted values/total values: 
  $$
  \frac{TP + TN}{TP + TN + FP + FN}
  $$

- **Precision:** Ratio of correctly predicted positives over total positive predictions: 
  $$
  \frac{TP}{TP + FP}
  $$

- **Recall:** Ratio of correctly predicted positives over all actual positives: 
  $$
  \frac{TP}{TP + FN}
  $$
  Also known as sensitivity.

- **F1 Score:** The harmonic mean of precision and recall that takes into account both FP and FN. It deals with the problem of imbalance where one class occurs more than the other.

$$
F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

- **Support:** The number of the actual appearances of a class in a dataset regardless of its classification: \(TP + FN\).

Analyzing the confusion matrix helps us understand the type of misclassifications that the model does, FP or FN. **FP** means the model is too lenient so it accepts more positives than it should and needs better precision. **FN** means the model is too strict and it needs better recall because it misses some positive values.

The use case matters such as whether the classification is used in the medical field (should be strict) or in spam filtering (more comprehensive).

**ROC Curve** is a plot between False Positive Rate (x) vs True Positive Rate (y) to identify the best threshold for the model to optimize the tradeoff. The best threshold lies closest to the top left corner. The larger the area under the curve, the better the model performance.

---

## 13. Logistic Regression

Logistic regression is used in classification to find the probability that a point belongs to a specific class. It uses logistic functions such as sigmoid to map the output of the linear combination (z) to a probability that lies between 0 and 1.

**Decision boundary** is a threshold that is used to decide when the point would be classified as 1 and when it would be classified as 0 based on the probability received from the logistic regression.

The loss function used in logistic regression to evaluate the model is:

$$
L(y, \hat{y}) = -[y \log(\hat{y}) + (1-y) \log(1-\hat{y})]
$$

**Gradient descent** is also used to optimize the weights and coefficients through iterations to find the best model.

Logistic regression also uses accuracy, precision, recall, F1, and ROC-AUC for evaluation metrics.

**Advantages:** It is easy to implement and interpret, outputs probability to show confidence, and is effective for binary classification.

**Disadvantages:** Assumes linear relationships, needs feature engineering for complex relationships, and struggles with multicollinearity (correlated features).

**Use cases:** Medicine (predict diseases), finance (detect fraud), cybersecurity (spam detection).

