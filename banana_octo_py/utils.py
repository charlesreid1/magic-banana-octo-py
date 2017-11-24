import numpy as np

def random_walk(N=100):
    return np.cumsum(np.random.randn(N), 0)
