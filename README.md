Customer Churn Prediction Project
Project Overview
This project aims to predict customer churn for a telecommunications company using the Telco Customer Churn dataset. By analyzing customer demographics, account information, and service usage, we develop a machine learning model to identify individuals at high risk of leaving the service.

Dataset Description
The dataset contains 7,043 rows and 21 columns. Key features include:

Demographics: Gender, Senior Citizen status, Partner, and Dependents.

Services: Phone service, Multiple lines, Internet service (DSL, Fiber optic), Online security, Tech support, and Streaming services.

Account Information: Tenure, Contract type, Payment method, Monthly charges, and Total charges.

Target: Churn (Yes/No).

Technical Workflow
1. Data Preprocessing & Cleaning
Type Conversion: Converted TotalCharges from an object type to numeric.

Missing Value Imputation: Identified missing values in TotalCharges and filled them using the median value of the column.

Categorical Encoding: Used One-Hot Encoding (pd.get_dummies) to transform categorical variables into a machine-readable format, resulting in 32 total features.

Binary Mapping: Mapped the target variable Churn to binary values: 1 for Yes and 0 for No.

2. Model Training
The data was split using a stratified 80/20 train-test split to ensure the churn distribution remained consistent. The primary model implemented was:

Algorithm: Logistic Regression.

Configuration: max_iter=1000 to ensure model convergence.

3. Evaluation Results
Accuracy: The model achieved an accuracy score of 80.34%.

Performance Metrics:

Precision (Churn): 0.65.

Recall (Churn): 0.56.

F1-Score (Churn): 0.60.

Confusion Matrix: Correct predictions included 924 non-churners and 208 churners.

Conclusions & Key Findings
The Logistic Regression model provides a strong baseline with ~80% accuracy.

The model is better at identifying customers who stay (recall: 0.89) than those who leave (recall: 0.56), indicating a need to address class imbalance in future iterations.

Future Work
Implement Hyperparameter Tuning for Decision Tree and Random Forest models.

Apply SMOTE (Synthetic Minority Over-sampling Technique) to improve the detection of churned customers.

Conduct deeper feature importance analysis to identify the top three drivers of customer churn.
