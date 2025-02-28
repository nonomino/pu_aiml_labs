import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import dual_annealing
from skfda.datasets import fetch_weather


data = fetch_weather()["data"]
temperatures = data[..., 0].T


def objective(threshold):
    return np.var(np.mean(temperatures, axis=1) - threshold)


bounds = [(-30, 30)] # Typical range
result = dual_annealing(objective, bounds)


plt.hist(np.mean(temperatures, axis=1), bins=20, alpha=0.7, label="Avg Temps")
plt.axvline(result.x[0], color="r", linestyle="--", label=f"Optimal Threshold: {result.x[0]:.2f}°C")
plt.legend()
plt.title("Simulated Annealing: Optimal Temperature Threshold")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()
print(f"Optimal Temperature Threshold: {result.x[0]:.2f}°C")