import numpy as np
from utils import optimizedConv2D

def gaborFilter(image, kernel):
    """
        Performing a gabor filter

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    return optimizedConv2D(image, kernel).astype(np.uint8)