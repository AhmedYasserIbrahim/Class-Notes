# Decision Trees in Machine Learning

Decision trees are structured like flowcharts and are commonly used in the field of machine learning. They can be applied to both **classification** (categorical outputs) and **regression** (continuous outputs) tasks. 

- The **root node** contains the entire dataset.  
- Each **internal node** represents a decision rule or a split based on a feature.  
- The **leaf nodes** represent the final prediction or class label after all splits.  

### ✅ Advantages:
- Simple to understand and implement.  
- Handles both numerical and categorical data.  
- **Pruning** can be used to remove unnecessary branches for efficiency.

### ❌ Disadvantages:
- **Overfitting:** Decision trees can become overly complex, fitting noise instead of the actual patterns.  
- **Sensitive to Noise:** Small changes in data can lead to significant changes in the tree structure.  

---

## 📊 Metrics to Evaluate Decision Trees:

To determine the quality of splits in a decision tree, we can use **Entropy** and **Gini Index**.

---

### **1. Entropy:**
- **Definition:** Entropy measures the level of **randomness** or **disorder** in a dataset.  
- If a group has mixed labels (`Yes` and `No`), the entropy is high. If all labels are the same, the entropy is low.  

**Formula for Entropy:**
\[
Entropy = -\sum_{i=1}^{C} p_i \log_2(p_i)
\]
where:  
- \(p_i\) is the probability of class \(i\)  
- \(C\) is the total number of classes  

**Information Gain:** Measures how much the disorder (entropy) is reduced after a split.  
\[
IG = Entropy_{Parent} - Entropy_{After Split}
\]

---

### **2. Gini Index:**
- **Definition:** Gini Index measures **impurity** in the data.  
- A **pure** dataset has a Gini index of **0** (all samples belong to one class).  
- The maximum Gini Index is **0.5** when classes are evenly split.

**Formula for Gini Index:**
\[
Gini = 1 - \sum_{i=1}^{C} p_i^2
\]

---

## 🎯 **Example: Will a Person Buy a Sports Car?**

| Age  | Income | Buys Sports Car? |
|------|--------|-----------------|
| ≤30  | High   | Yes             |
| ≤30  | Low    | No              |
| 31-40| Medium | Yes             |
| >40  | High   | No              |
| >40  | Low    | No              |

**Step 1: Calculate Initial Entropy (Before Splitting)**  
- **Yes:** 2 out of 5 → \(p_{Yes} = \frac{2}{5}\)  
- **No:** 3 out of 5 → \(p_{No} = \frac{3}{5}\)  

\[
Entropy = -\left(\frac{2}{5}\log_2\frac{2}{5} + \frac{3}{5}\log_2\frac{3}{5}\right)  
\approx 0.970
\]

---

**Step 2: Splitting by Age and Calculating Entropy of Groups:**

- **Age ≤ 30:** [Yes, No] → Entropy = 1  
- **Age 31-40:** [Yes] → Entropy = 0  
- **Age > 40:** [No, No] → Entropy = 0  

**Weighted Entropy After Splitting:**
\[
Entropy_{Age} = \frac{2}{5} \times 1 + \frac{1}{5} \times 0 + \frac{2}{5} \times 0 = 0.4
\]

---

**Step 3: Information Gain:**
\[
IG_{Age} = 0.970 - 0.4 = 0.570
\]

---

**Step 4: Gini Index (Before Splitting):**
\[
Gini = 1 - \left(\frac{2}{5}^2 + \frac{3}{5}^2\right) = 1 - (0.16 + 0.36) = 0.48
\]

---

### ✅ **Conclusion:**
- Splitting by **Age** reduces the entropy and the Gini Index.  
- Decision trees split on features that result in the **lowest entropy** or **Gini Index** to make the data as pure as possible.  
- **Information Gain** helps identify the most effective split by showing the reduction in disorder.

**Decision Tree Final Structure:**
```
           Age
         /   |   \
     ≤30    31-40   >40
    /   \      |      /   \
 Yes    No    Yes    No    No
```
