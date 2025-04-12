import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import dual_annealing

file_path = "../data/canada_weather.csv"
df = pd.read_csv(file_path)

high_temps = df.iloc[:, 4].str.extract(r'([-\d.]+)').astype(float)[0]
low_temps = df.iloc[:, 5].str.extract(r'([-\d.]+)').astype(float)[0]

temperatures = np.vstack([high_temps, low_temps])


def objective(threshold):
    return np.var(np.mean(temperatures, axis=0) - threshold)


bounds = [(-30, 30)]
result = dual_annealing(objective, bounds)

plt.hist(np.mean(temperatures, axis=0), bins=20, alpha=0.7, label="Avg Temps")
plt.axvline(result.x[0], color="r", linestyle="--", label=f"Optimal Threshold: {result.x[0]:.2f}°C")
plt.legend()
plt.title("Simulated Annealing: Optimal Temperature Threshold")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()

print(f"Optimal Temperature Threshold: {result.x[0]:.2f}°C")
