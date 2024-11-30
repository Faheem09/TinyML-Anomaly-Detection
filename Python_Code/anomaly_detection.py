import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv("vibration_data.csv")

# Train Unsupervised Model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(data)

# Detect Anomalies
data["anomaly"] = model.predict(data)
data["anomaly"] = data["anomaly"].apply(lambda x: 1 if x == -1 else 0)

# Visualize Anomalies
plt.figure(figsize=(10, 6))
plt.plot(data.index, data["x"], label="x-axis")
plt.scatter(data.index[data["anomaly"] == 1], 
            data["x"][data["anomaly"] == 1], color="red", label="Anomalies")
plt.legend()
plt.title("Vibration Data with Anomalies")
plt.show()
