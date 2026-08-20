# Import Libraries
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest # Corrected import

# Load Dataset from a public URL
uci_diabetes = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv")

# Perform Z-Test for Glucose (Testing if mean Glucose differs from 100)
z_stat, p_value = ztest(uci_diabetes["Glucose"], value=100)

# Display Results
print(f"Z-Statistic: {z_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

# Interpretation
alpha = 0.05 # 5% significance level
if p_value < alpha:
    print("Reject the null hypothesis: The mean Glucose level is significantly different from 100.")
else:
    print("Fail to reject the null hypothesis: No significant difference in mean Glucose level.")