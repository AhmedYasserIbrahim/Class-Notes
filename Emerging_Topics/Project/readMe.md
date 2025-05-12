# Network Traffic Malware Detection & Visualization

## 🚀 Project Overview

This project delivers a comprehensive machine-learning pipeline and interactive dashboard for detecting and visualizing malicious network traffic. It processes raw NetFlow-style data, engineers robust features, trains high-performance classifiers, and provides real-time analytics and alerting via a Streamlit interface.

### Key Components

* **Data Ingestion & Preprocessing**
  Handles misaligned headers, large-scale missing values, one-hot encoding for categorical fields, IP address embeddings, temporal feature extraction, and feature scaling with an 80/20 stratified split.
* **Machine Learning Models**

  * **Binary Classification**: Logistic Regression vs. Multilayer Perceptron (MLP) to distinguish benign from malicious traffic.
  * **Multiclass Classification**: Decision Tree and Random Forest to label flows as `botnet_v1`, `zeus`, or `ddos`.
* **Interactive Dashboard**
  Built with Streamlit, Seaborn, and Matplotlib to showcase correlation heatmaps, performance charts, and a live table of flagged malicious flows labeled by malware type.

## 📈 Evaluation Highlights

* **Logistic Regression (Binary)**: achieved high precision and recall, reliably detecting malicious entries.
* **Multilayer Perceptron (Binary)**: delivered near-perfect accuracy on the binary detection task.
* **Decision Tree & Random Forest (Multiclass)**: produced identical near-perfect metrics, indicating dataset simplicity or potential overfitting.
  Detailed precision, recall, and F1-score values are available in the accompanying notebook.

## 🔍 Roadmap

* Incorporate clustering visualizations (e.g., K-Means) to reveal traffic subgroups.
* Integrate Elasticsearch for scalable, real-time data ingestion and search.
* Add hyperparameter tuning and cross-validation workflows.
* Dockerize the pipeline and dashboard for simplified deployment.

## 🔗 Project Link

[Milestone Project Notebook](https://github.com/AhmedYasserIbrahim/Class-Notes/blob/main/Emerging_Topics/Project/Milestone_Project.ipynb)
