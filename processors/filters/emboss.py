import numpy as np
from utils import optimizedConv2D

def emboss(image):
    embossKernel = np.array([
        [-2, -1, 0],
        [-1,  1, 1],
        [ 0,  1, 2]
    ])
    return optimizedConv2D(image, embossKernel).clip(0, 255)