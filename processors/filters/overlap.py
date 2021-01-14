import numpy as np
from numpy import math

def overlap(image, overlapper):
    return np.minimum(image, overlapper)