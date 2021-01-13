from utils import conv2D
import numpy as np

def increasedEdgeEnhancement(image):
    increasedEdgeEnhanceKernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ], np.float32)

    return conv2D(image, increasedEdgeEnhanceKernel)

