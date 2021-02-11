from utils import optimizedConv2D
import numpy as np

def sharpen(image):
    """
        Performing a sharpening filter

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    increasedEdgeEnhanceKernel = np.array([
        [ 0, -1,  0],
        [-1,  5, -1],
        [ 0, -1,  0]
    ], np.float32)

    return optimizedConv2D(image, increasedEdgeEnhanceKernel).clip(0, 255)

def unsharp(image):
    """
        Performing an unsharpening filter

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    increasedEdgeEnhanceKernel = np.array([
        [1,   4,     6,  4, 1],
        [4,  16,    24, 16, 4],
        [6,  24,  -476, 24, 6],
        [4,  16,    24, 16, 4],
        [1,   4,     6,  4, 1]
    ], np.float32) * -1.0 / 256

    return optimizedConv2D(image, increasedEdgeEnhanceKernel).clip(0, 255)
