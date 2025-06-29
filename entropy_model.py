
import numpy as np

def theta(t, gammas):
    return np.sum(np.exp(-t * gammas**2))
