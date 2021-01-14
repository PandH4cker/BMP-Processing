import numpy as np
from utils import conv2D

def emboss(image):
    embossKernel = np.array([
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ])
    return conv2D(image, embossKernel)