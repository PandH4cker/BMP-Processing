import numpy as np
from utils import optimizedConv2D

def gaborFilter(image, kernel):
    return optimizedConv2D(image, kernel).astype(np.uint8)