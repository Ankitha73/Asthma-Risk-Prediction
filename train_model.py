import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("AirQuality.csv", sep=';')

# Select columns
data = data[['T', 'RH', 'NO2(GT)']]

# Rename columns
data.columns = ['temperature', 'humidity', 'aqi']

# Remove missing values
data = data.dropna()

# Create risk labels
risk = []

for i in data['aqi']:

    if i < 50:
        risk.append("Low")

    elif i < 100:
        risk.append("Medium")

    else:
        risk.append("High")

# Add risk column
data['risk'] = risk

# Inputs
X = data[['temperature', 'humidity', 'aqi']]

# Output
y = data['risk']

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "risk_model.pkl")

print("Model trained successfully")