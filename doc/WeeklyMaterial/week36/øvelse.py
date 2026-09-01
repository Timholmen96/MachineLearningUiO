import numpy as np

def covariance(x,y):
    """ Sample covariance of two vectors, 
    using the 1/n convention"""
    cov = np.mean((x - np.mean(x)) * (y - np.mean(y)))
    return cov
rng = np.random.default_rng(2024)
n = 1000
x = rng.normal(size=n)
y = 4.0 + 3.0 * x + rng.normal(size=n) # correlated with x
z = rng.normal(size=n) # independent of both 

cov_xy = covariance(x,y)
cov_xz = covariance(x,z)
print(f"Covariance of x and y: {cov_xy:.4f}")
print(f"Covariance of x and z: {cov_xz:.4f}")

tripe_cov = np.cov((np.vstack((x,y,z))))
corr = np.corrcoef((np.vstack((x,y,z))))
print(f"Covariance matrix:\n{tripe_cov}")
print(f"Correlation matrix:\n{corr}")


temps = np.array([30, 32, 31, 29, 28, 27, 26])
day_i_temps = temps[1:]
day_i_minus_1_temps = temps[:-1]
print(day_i_temps)
print(day_i_minus_1_temps)