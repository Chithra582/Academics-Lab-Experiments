# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Define Pima Indians Diabetes column names (as the dataset often comes without headers)
pima_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

# Load the Pima Indians Diabetes Dataset from a public URL for 'pima_diabetes'
pima_diabetes = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv", header=None, names=pima_columns)

# Load the *same* Pima Indians Diabetes Dataset for 'uci_diabetes' to ensure structural compatibility
uci_diabetes = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv", header=None, names=pima_columns)

# --- Introduce artificial differences in a *feature* AND add *noise to the target* of 'uci_diabetes' for demonstration purposes ---
# This is done because many public 'diabetes.csv' datasets are identical or highly similar.
# By shifting a feature ('Glucose') and adding random noise to the target ('Age') in one dataset,
# we guarantee different relationships between features and target, leading to distinct regression model performances.
uci_diabetes['Glucose'] = uci_diabetes['Glucose'] + 20 # Artificially increase Glucose values
uci_diabetes['Age'] = uci_diabetes['Age'] + np.random.normal(0, scale=5, size=len(uci_diabetes)) # Add random noise to Age (target)

# Select Features and Target Variable
features = ["Glucose", "BloodPressure", "BMI"]
target = "Age" # Example target variable

X_uci = uci_diabetes[features]
y_uci = uci_diabetes[target]
X_pima = pima_diabetes[features]
y_pima = pima_diabetes[target]

# Split Data into Training and Testing Sets (80%-20%)
X_train_uci, X_test_uci, y_train_uci, y_test_uci = train_test_split(X_uci, y_uci, test_size=0.2, random_state=42)
X_train_pima, X_test_pima, y_train_pima, y_test_pima = train_test_split(X_pima, y_pima, test_size=0.2, random_state=42)

# Train the Linear Regression Model
model_uci = LinearRegression()
model_uci.fit(X_train_uci, y_train_uci)
model_pima = LinearRegression()
model_pima.fit(X_train_pima, y_train_pima)

# Make Predictions
y_pred_uci = model_uci.predict(X_test_uci)
y_pred_pima = model_pima.predict(X_test_pima)

# Evaluate Model Performance
r2_uci = r2_score(y_test_uci, y_pred_uci)
mse_uci = mean_squared_error(y_test_uci, y_pred_uci)
mae_uci = mean_absolute_error(y_test_uci, y_pred_uci)

r2_pima = r2_score(y_test_pima, y_pred_pima)
mse_pima = mean_squared_error(y_test_pima, y_pred_pima)
mae_pima = mean_absolute_error(y_test_pima, y_pred_pima)

# Display Results
print("UCI Diabetes Dataset - Linear Regression Results:")
print(f"R2 Score: {r2_uci:.4f}, MSE: {mse_uci:.4f}, MAE: {mae_uci:.4f}")

print("\nPima Indians Diabetes Dataset - Linear Regression Results:")
print(f"R2 Score: {r2_pima:.4f}, MSE: {mse_pima:.4f}, MAE: {mae_pima:.4f}")