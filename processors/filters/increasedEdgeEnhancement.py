from utils import optimizedConv2D
import numpy as np

def increasedEdgeEnhancement(image):
    """
        Performing an increased edge enhancement filter

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    increasedEdgeEnhanceKernel = np.array([
        [-1, -1, -1],
        [-1,  9, -1],
        [-1, -1, -1]
    ], np.float32)

    return optimizedConv2D(image, increasedEdgeEnhanceKernel).clip(0, 255)

