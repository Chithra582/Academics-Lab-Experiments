import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

# 1. Create a synthetic temporary dataset
np.random.seed(42)
dates = pd.date_range(start="2026-01-01", periods=100, freq="D")
# Generate synthetic glucose values around a mean of 120 with a slight trend and noise
base_glucose = 120 + np.sin(np.linspace(0, 4 * np.pi, 100)) * 15 + np.linspace(0, 10, 100)
noise = np.random.normal(0, 5, 100)
glucose_levels = base_glucose + noise

# Assign to temporary DataFrame
diabetes_data = pd.DataFrame({"Glucose": glucose_levels}, index=dates)

# 2. Plot Original Series & Moving Average Smoothing
diabetes_data["Glucose_MA"] = diabetes_data["Glucose"].rolling(window=7).mean()

plt.figure(figsize=(10, 4))
plt.plot(diabetes_data["Glucose"], label="Original", alpha=0.5)
plt.plot(diabetes_data["Glucose_MA"], label="7-day Moving Average", color="orange")
plt.title("Glucose Levels - Moving Average Smoothing")
plt.xlabel("Date")
plt.ylabel("Glucose Level")
plt.legend()
plt.tight_layout()
plt.show()

# 3. Seasonal Decomposition (Additive)
decomposition = seasonal_decompose(diabetes_data["Glucose"], model="additive", period=7)
fig, axes = plt.subplots(3, 1, figsize=(10, 6), sharex=True)
decomposition.trend.plot(ax=axes[0], title="Trend Component")
decomposition.seasonal.plot(ax=axes[1], title="Seasonal Component")
decomposition.resid.plot(ax=axes[2], title="Residual Component")
plt.tight_layout()
plt.show()

# 4. Fit ARIMA Model & Plot Forecast
train_size = int(len(diabetes_data) * 0.8)
train = diabetes_data["Glucose"][:train_size]
test = diabetes_data["Glucose"][train_size:]

model = ARIMA(train, order=(5, 1, 0))
fitted_model = model.fit()

forecast = fitted_model.forecast(steps=len(test))

plt.figure(figsize=(10, 4))
plt.plot(train.index, train, label="Train", color="blue")
plt.plot(test.index, test, label="Actual (Test)", color="gray")
plt.plot(test.index, forecast, label="ARIMA Forecast", color="red", linestyle="--")
plt.title("ARIMA Model Forecasting on Temporary Dataset")
plt.xlabel("Date")
plt.ylabel("Glucose Level")
plt.legend()
plt.tight_layout()
plt.show()