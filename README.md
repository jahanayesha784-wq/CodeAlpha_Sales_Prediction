# Sales Prediction with Machine Learning

A machine learning project developed as part of the **CodeAlpha Data Science Internship — Task 4**.

The project analyzes advertising expenditure across **TV, Radio, and Newspaper** channels and builds regression models to predict sales.

## Project Overview

The objective of this project is to understand how advertising investment relates to sales and develop a machine learning model capable of predicting sales from advertising budgets.

The project covers:

* Data loading and cleaning
* Exploratory Data Analysis (EDA)
* Correlation analysis
* Outlier analysis
* Regression modeling
* Model comparison
* Cross-validation
* Hyperparameter tuning
* Prediction error analysis
* Feature importance analysis
* Model deployment with Streamlit

## Dataset

The project uses the `Advertising.csv` dataset containing 200 observations.

### Features

| Feature   | Description                          |
| --------- | ------------------------------------ |
| TV        | Advertising expenditure on TV        |
| Radio     | Advertising expenditure on Radio     |
| Newspaper | Advertising expenditure on Newspaper |
| Sales     | Target variable representing sales   |

## Machine Learning Models

The following regression models were evaluated:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Random Forest Regressor
5. Gradient Boosting Regressor

### Model Evaluation

Models were evaluated using:

* MAE — Mean Absolute Error
* MSE — Mean Squared Error
* RMSE — Root Mean Squared Error
* R² — Coefficient of Determination
* 5-Fold Cross-Validation

## Cross-Validation Results

The initial 5-fold cross-validation produced:

| Model             | Mean CV R² |
| ----------------- | ---------: |
| Gradient Boosting |     0.9807 |
| Random Forest     |     0.9805 |
| Lasso Regression  |     0.8829 |
| Ridge Regression  |     0.8827 |
| Linear Regression |     0.8827 |

Gradient Boosting achieved the highest mean cross-validation R² among the evaluated models.

## Hyperparameter Tuning

GridSearchCV was used to optimize the Gradient Boosting model.

Best parameters obtained:

```text
n_estimators = 200
learning_rate = 0.05
max_depth = 3
min_samples_split = 2
min_samples_leaf = 2
```

The final model was retrained using the complete cleaned dataset before deployment.

## Exploratory Data Analysis

The project includes:

* Sales distribution analysis
* Advertising vs Sales scatter plots
* Correlation heatmap
* Outlier analysis
* Actual vs Predicted visualization
* Residual analysis
* Prediction error distribution
* Feature importance analysis

## Feature Importance

Gradient Boosting feature importance was used to investigate which advertising channels the model relied on most when predicting sales.

This analysis should be interpreted as **model-based importance rather than causal impact**.

## Streamlit Application

The trained model is deployed through a Streamlit web application.

The application allows users to enter:

* TV advertising expenditure
* Radio advertising expenditure
* Newspaper advertising expenditure

and receive a predicted sales value.

### Application Features

* Clean responsive interface
* Pink and purple gradient UI
* Interactive input fields
* Machine learning prediction
* Trained Gradient Boosting model
* Real-time prediction

## Project Structure

```text
CodeAlpha_Sales_Prediction/
│
├── data/
│   └── Advertising.csv
│
├── models/
│   └── sales_prediction_model.pkl
│
├── notebooks/
│   └── sales_prediction.ipynb
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd CodeAlpha_Sales_Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit
* Jupyter Notebook
* Git & GitHub

## Internship Task

**CodeAlpha Data Science Internship**

**Task 4 — Sales Prediction using Python**

The project demonstrates the complete machine learning workflow from data preprocessing and exploratory analysis to model training, evaluation, optimization, and deployment.

## Author

**Aisha Noor**

Data Science Student
IMSciences University of Peshawar
