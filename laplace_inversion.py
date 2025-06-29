
import numpy as np
from scipy.optimize import least_squares

def model_theta(t, x):
    return np.sum(np.exp(-np.outer(t, x**2)), axis=1)

def recover_zeros(t_values, theta_values, N=10):
    x0 = np.linspace(10, 50, N)
    result = least_squares(lambda x: model_theta(t_values, x) - theta_values, x0, bounds=(0, 100))
    return np.sort(result.x)
