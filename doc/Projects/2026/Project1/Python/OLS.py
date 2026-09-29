import numpy as np
import matplotlib.pyplot as plt

def runge(x):
    return 1.0 / (1.0 + 25.0 * x**2)

def design_matrix(x, degree, intercept=True):
    # polynomial features [1, x, x^2, ..., x^degree] (drop the 1 if intercept=False)
    start = 0 if intercept else 1
    return np.vstack([x**p for p in range(start, degree + 1)]).T

rng = np.random.default_rng(2026)
n = 100
sigma = 0.1                                  # noise level: explore it!
x = np.sort(rng.uniform(-1, 1, n))
y = runge(x) + sigma*rng.normal(0, sigma, n)

xx = np.linspace(-1, 1, 400)

# Your code for part a) here
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

maxdeg = 15
deg_V = np.arange(maxdeg + 1)
MSE_V = []
R2_V = []
Parameter_V = []
Prediction_V = []

# No reason to scale and normalise for OLS
for degree in range(maxdeg + 1):
    X = design_matrix(x, degree)
    X_train, X_test, y_train, y_test = train_test_split(X,
    y, test_size=0.3, random_state=2026)

    theta = np.linalg.pinv(X_train) @ y_train
    Parameter_V.append(theta)
    if degree == 5:
        print(theta)

    X_plot = design_matrix(xx, degree)
    Prediction_V.append(X_plot @ theta)

    y_predict = X_test @ theta
    mse = np.mean((y_test - y_predict)**2)
    MSE_V.append(mse)

    y_mean = np.mean(y_test)
    R2 = 1 - (np.sum((y_test - y_predict)**2))/(np.sum((y_test - y_mean)**2))
    #R2 = r2_score(y_test, y_predict)
    R2_V.append(R2)

fig, (ax_parameters, ax_predictions) = plt.subplots(1, 2, figsize=(13, 5))

# Grad d har d + 1 parametre. NaN markerer parametre modellen ikke har.
parameters = np.full((maxdeg + 1, maxdeg + 1), np.nan)
for degree, theta in enumerate(Parameter_V):
    parameters[degree, :len(theta)] = theta
    ax_predictions.plot(xx, Prediction_V[degree], label=f"Degree {degree}")

for j in range(maxdeg + 1):
    ax_parameters.plot(deg_V, parameters[:, j], marker="o", label=rf"$\theta_{j}$")

ax_parameters.set(title="Parameters vs degree", xlabel="Polynomial degree",
                  ylabel="Coefficient (standardized features)")
ax_parameters.set_xticks(deg_V)
ax_parameters.legend()
ax_parameters.grid(alpha=0.3)

ax_predictions.scatter(x, y, s=15, color="gray", alpha=0.5, label="Data")
ax_predictions.plot(xx, runge(xx), "k--", label="Runge function")
ax_predictions.set(title="Predictions for each degree", xlabel="x", ylabel="y")
ax_predictions.legend()
ax_predictions.grid(alpha=0.3)
fig.tight_layout()
plt.ylim(-1,1)
plt.show()

plt.scatter(deg_V, MSE_V, label = "MSE")
plt.scatter(deg_V[0:-2], R2_V[0:-2], label = f"R2, degree 15 = {R2_V[-1]:.2f}")
plt.xlabel("Degree")
plt.ylabel("Score")
plt.legend()
plt.grid()
plt.show()

