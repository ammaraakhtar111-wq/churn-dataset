# Customer Churn Prediction - Machine Learning Project

**Author:** Ammara Akhtar  
**Course:** Introduction to Applied Artificial Intelligence  
**Semester:** BS 8th Semester  
**Labs:** Week 1 & Week 2 - Customer Churn Prediction  

---

## Project Overview

This project aims to predict **customer churn** for a telecom company using machine learning models. The main objectives are:

- Preprocess the dataset and handle missing values  
- Encode categorical variables into numeric features  
- Train and evaluate multiple machine learning models:
  - Logistic Regression
  - Decision Tree
  - Random Forest  
- Compare model performance and identify the best model  
- Engineer new features to improve predictions  

---

## Dataset

The dataset contains customer information such as:

- Demographics: gender, partner, dependents  
- Services subscribed: phone, internet, streaming, etc.  
- Account information: tenure, contract type, monthly charges, total charges  
- Target variable: `Churn` (Yes/No)  

**Source:** [WA_Fn-UseC_-Telco-Customer-Churn.csv]

---

## Project Structure

- **week1_eda.ipynb** — Exploratory Data Analysis (EDA) from Week 1  
- **week2_ml_models.ipynb** — Jupyter notebook with preprocessing, models, evaluation, and feature engineering  
- **README.md** — Project description and summary  

---

## Data Preprocessing

- Converted `TotalCharges` to numeric and filled missing values with median  
- Encoded categorical variables using one-hot encoding  
- Converted target variable `Churn` to numeric (Yes=1, No=0)  

---

## Machine Learning Models

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression  | 0.78     |
| Decision Tree        | 0.74     |
| Random Forest        | 0.81     |

- **Best Model:** Random Forest  

---

## Feature Engineering

Additional features were created to improve prediction:

1. **TotalRevenue** = tenure × monthly charges  
2. **TotalServices** = count of services subscribed  
3. **TenureGroup** = grouping customers by tenure  
4. **HighCharges** = flag for customers with high monthly charges  

---

## Key Findings

- Customers on **month-to-month contracts** are more likely to churn  
- Higher **Monthly Charges** increase churn risk  
- Contract type, tenure, and monthly charges are the most important features  
- Feature engineering slightly improved model performance  

---

## How to Run

1. Clone this repository:  
```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
