import numpy as np

"Measures of quality"

"Mean squared error"
def mse(y,y_tide):
    return np.mean((y-y_tilde)**2)

"Coefficient of determination"
def r2(y,y_tilde):
    return 1.0 - np.sum((y - y_tilde)**2) / np.sum((y - np.mean(y))**2)

"Mean absolute error"
def mae(y, y_tilde):
    return np.mean(np.abs(y-y_tilde))

"Only meaningful on test data"