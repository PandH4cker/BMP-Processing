from utils import optimizedConv2D
import numpy as np

def sharpen(image):
    increasedEdgeEnhanceKernel = np.array([
        [ 0, -1,  0],
        [-1,  5, -1],
        [ 0, -1,  0]
    ], np.float32)

    return optimizedConv2D(image, increasedEdgeEnhanceKernel).clip(0, 255)

def unsharp(image):
    increasedEdgeEnhanceKernel = np.array([
        [1,   4,     6,  4, 1],
        [4,  16,    24, 16, 4],
        [6,  24,  -476, 24, 6],
        [4,  16,    24, 16, 4],
        [1,   4,     6,  4, 1]
    ], np.float32) * -1.0 / 256

    return optimizedConv2D(image, increasedEdgeEnhanceKernel).clip(0, 255)
