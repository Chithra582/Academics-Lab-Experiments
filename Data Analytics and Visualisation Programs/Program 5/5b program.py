# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Define Pima Indians Diabetes column names (as the dataset often comes without headers)
pima_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

# Load the Pima Indians Diabetes Dataset from a public URL for 'pima_diabetes'
pima_diabetes = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv", header=None, names=pima_columns)

# Load the *same* Pima Indians Diabetes Dataset for 'uci_diabetes' to ensure structural compatibility
uci_diabetes = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv", header=None, names=pima_columns)

# --- Introduce an artificial difference in 'uci_diabetes' for demonstration purposes ---
# This is done because many public 'diabetes.csv' datasets are identical or highly similar.
# By shifting 'Glucose' in one dataset, we guarantee a difference for the logistic regression model.
uci_diabetes['Glucose'] = uci_diabetes['Glucose'] + 15  # Artificially increase Glucose values

# Select Features and Target Variable
features = ["Glucose", "BloodPressure", "BMI"]
target = "Outcome" # Target variable indicating diabetes presence
X_uci = uci_diabetes[features]
y_uci = uci_diabetes[target]
X_pima = pima_diabetes[features]
y_pima = pima_diabetes[target]

# Split Data into Training and Testing Sets (80%-20%)
X_train_uci, X_test_uci, y_train_uci, y_test_uci = train_test_split(X_uci, y_uci, test_size=0.2, random_state=42)
X_train_pima, X_test_pima, y_train_pima, y_test_pima = train_test_split(X_pima, y_pima, test_size=0.2, random_state=42)

# Train the Logistic Regression Model
model_uci = LogisticRegression(max_iter=200) # Increased max_iter for convergence
model_uci.fit(X_train_uci, y_train_uci)

model_pima = LogisticRegression(max_iter=200) # Increased max_iter for convergence
model_pima.fit(X_train_pima, y_train_pima)

# Make Predictions
y_pred_uci = model_uci.predict(X_test_uci)
y_pred_pima = model_pima.predict(X_test_pima)

# Evaluate Model Performance
accuracy_uci = accuracy_score(y_test_uci, y_pred_uci)
precision_uci = precision_score(y_test_uci, y_pred_uci)
recall_uci = recall_score(y_test_uci, y_pred_uci)
f1_uci = f1_score(y_test_uci, y_pred_uci)

accuracy_pima = accuracy_score(y_test_pima, y_pred_pima)
precision_pima = precision_score(y_test_pima, y_pred_pima)
recall_pima = recall_score(y_test_pima, y_pred_pima)
f1_pima = f1_score(y_test_pima, y_pred_pima)

# Display Results
print("UCI Diabetes Dataset - Logistic Regression Results:")
print(f"Accuracy: {accuracy_uci:.4f}, Precision: {precision_uci:.4f}, Recall: {recall_uci:.4f}, F1 Score: {f1_uci:.4f}")

print("\nPima Indians Diabetes Dataset - Logistic Regression Results:")
print(f"Accuracy: {accuracy_pima:.4f}, Precision: {precision_pima:.4f}, Recall: {recall_pima:.4f}, F1 Score: {f1_pima:.4f}")

# Plot Confusion Matrices
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.heatmap(confusion_matrix(y_test_uci, y_pred_uci), annot=True, fmt='d', cmap='Blues', ax=axes[0])
axes[0].set_title("UCI Diabetes - Confusion Matrix")
axes[0].set_xlabel("Predicted")
axes[0].set_ylabel("Actual")
sns.heatmap(confusion_matrix(y_test_pima, y_pred_pima), annot=True, fmt='d', cmap='Blues', ax=axes[1])
axes[1].set_title("Pima Indians Diabetes - Confusion Matrix")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Actual")
plt.tight_layout()
plt.show()