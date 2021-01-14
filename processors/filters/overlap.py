import numpy as np
from numpy import math

def sigmoid(x):
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = 1 / (1 + math.exp(-x[i]))
    return y

def overlap(image, overlapper):
    """s = sigmoid(np.arange(-1, 1, 1/50))
    alpha = np.repeat(s.reshape((len(s), 1)), repeats=512, axis=1)
    return image * (1.0 - alpha) + overlapper * alpha"""
    return np.minimum(image, overlapper)