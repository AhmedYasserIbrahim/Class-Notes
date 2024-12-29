# AI and Data Science Final

Below are the answers to the questions provided in the final exam, reflecting key concepts in AI and Data Science.

---

### Q1:
- **Interpretation of the slope**: A slope of 12 indicates that an increase in the advertising spend by one unit increases the monthly sales by 12, indicating a strong relationship.
- **Intercept meaning**: The intercept represents the baseline prediction of the model. It means that if the advertising spend is zero, the predicted monthly sales would be 200.
- **R-squared value**: The R-squared value of 0.85 represents the percentage of variation in the monthly sales that is captured by the model, indicating that the model can make accurate predictions.
- **Standard error**: The standard error of the estimate tells us that, on average, the model’s prediction would be 50 units off the monthly sales. In this case, the standard error could be considered moderate and acceptable given the predictions.
- **P-value**: The p-value is 0.001 (0.05) which indicates that the feature advertising spend is a good predictor that significantly affects the value of the monthly sales.

---

### Q2:
1. The classifier performs well when predicting positive reviews, which is indicated by the F1 score value of 0.76. This value represents a harmonic mean of precision and recall and is used to evaluate the overall performance of the model. The model’s ability to predict positive reviews was moderate, given its F1 score of 0.66 on precision and recall, even though it could be considered low depending on the use case. The model struggles with predicting neutral reviews, which is indicated by the low F1 score of 0.53 and low precision and recall.
2. For the positive predictions, the model made fewer misclassifications than predicting neutral reviews, with most of the misclassified values. The performance of the model when predicting negative values was lower as it had many neutral reviews predicted as negative. The model exhibited poor performance when predicting the neutral reviews, with 15 of them being positive in reality and 25 of them being negative.
3. The model could benefit greatly from reducing the misclassified data, particularly neutral reviews. This would also reflect positively on the positive and negative reviews that were misclassified as neutral. Another approach would be to use a more complex model that can capture the underlying patterns to improve the accuracy of the model classifications.

---

### Q3:
1. Optimizing convex functions is easier and yields better results as convex functions have only one local minimum that is also a global minimum. This means that the model would always converge to the optimal solution.
2. Gradient descent is an optimization algorithm that improves the accuracy of the parameters of the model iteratively. In every iteration, it calculates the gradient of the loss function given the current parameter and makes a prediction in the opposite direction of the steepest ascent. This helps find better parameters for the model to the minimum point, indicating lower errors. It is also affected by the value of the learning rate that is set.
3. In non-convex functions, the function tends to have multiple local minima, which means that the function may converge towards a local minimum that is not the global minimum, so it would not reach the optimal solution. Nevertheless, gradient descent should provide low error and high accuracy in non-convex settings, even if it is imperfect.
4. In a logistic regression problem, gradients are calculated by using a loss function where the partial differentiation is used to compute the gradient for every weight and coefficient in the logistic regression function. The prediction for the new parameter is chosen in the direction opposite to the sharpest ascent in the gradient for each coefficient. This allows computing a parameter that is closer to the minimal value in the gradient, meaning that it has less error than the original parameter used. Iterations are repeated until optimal or near-optimal parameters are reached.

---

### Q4:
1. Model A exhibits low training error and higher testing error. This indicates that the model might suffer from overfitting, as it memorizes the patterns in the training data. It does not only learn the underlying patterns but also the noise in the training data. This results in the model not being able to generalize well to unseen data, yielding high testing error.
2. Model B exhibits consistent error rates between training and testing data. This means that the performance of the model is consistent, and it would generalize well to unseen data. However, if the errors are too high, this might indicate that the model is underfitting and it does not learn the underlying patterns well.

---

### Q5:
1. To improve Model B, we may use new complex models that are able to better catch any underlying patterns in the data.
2. Another approach would be to impose a penalty for the coefficients in the model. This would result in a less complex model that does not memorize the training data, yielding better generalization to unseen data.
3. Another approach could be cross-validation that divides the data into subsets and uses every subset for training once. Then, the model with the lowest testing error would be selected as the final model to improve accuracy.

---

### Q6:
1. Principal component analysis can help capture the most relevant features of the data by performing dimensionality reduction, as it reduces the features, some of which might be highly correlated, to principal components. Every component expresses a variance percentage. By capturing the highest eigenvalues, the model captures most variation and reduces the number of features without having redundancy that might affect the performance of the model.
2. The number of features to retain depends on the explained variance ratio, which determines the percentage of variance captured by every principal component. We choose the number of principal components whose explained variance ratios sum to a sufficient percentage of the total variance to train an ideal model.
3. It is necessary to maintain a balance in the number of features selected as selecting too many components would result in having redundancy in the data, which means that some features might affect the model more than others. It would also result in features generating confusion as selecting too few components might result in losing too much of the variation in the data. This means that some necessary features that affect the model would not be selected, leading to inaccurate predictions by the model as it misses some patterns.

---

End of answers.
