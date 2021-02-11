import numpy as np
from utils import conv2D, optimizedConv2D

def simpleBlur(image):
    """
        Apply a simple blur on the image

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    simpleBlurKernel = np.ones((3, 3)) * 1.0 / 9
    return optimizedConv2D(image, kernel=simpleBlurKernel)

def blurMore(image):
    """
        Apply a more blur on the image

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    return simpleBlur(simpleBlur(image))

def averageBlur(image):
    """
        Apply an average blur on the image

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    averageBlurKernel = np.ones((5, 5)) * 1.0 / 25
    return optimizedConv2D(image, averageBlurKernel)

def gaussianBlur(image):
    """
        Apply a gaussian blur on the image

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    gaussianBlurKernel = np.array([
        [2,  4,  5,  4, 2],
        [4,  9, 12,  9, 4],
        [5, 12, 15, 12, 5],
        [4,  9, 12,  9, 4],
        [2,  4,  5,  4, 2]
    ]) * 1.0 / 159
    return optimizedConv2D(image, gaussianBlurKernel)

def motionBlur(image):
    """
        Apply a motion blur on the image

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    motionBlurKernel = np.array([
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1]
    ]) * 1.0 / 9
    return optimizedConv2D(image, motionBlurKernel)

"""
    Switch definition to simplify the code.
"""
switcher = {
    'simple': simpleBlur,
    'more': blurMore,
    'average': averageBlur,
    'gaussian': gaussianBlur,
    'motion': motionBlur
}