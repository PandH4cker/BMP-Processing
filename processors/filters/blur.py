import numpy as np
from utils import conv2D, optimizedConv2D

def simpleBlur(image):
    simpleBlurKernel = np.ones((3, 3)) * 1.0 / 9
    return optimizedConv2D(image, kernel=simpleBlurKernel)
    #return conv2D(image, simpleBlurKernel)

def blurMore(image):
    return simpleBlur(simpleBlur(image))

def averageBlur(image):
    averageBlurKernel = np.ones((5, 5)) * 1.0 / 25
    return optimizedConv2D(image, averageBlurKernel)

def gaussianBlur(image):
    gaussianBlurKernel = np.array([
        [2,  4,  5,  4, 2],
        [4,  9, 12,  9, 4],
        [5, 12, 15, 12, 5],
        [4,  9, 12,  9, 4],
        [2,  4,  5,  4, 2]
    ]) * 1.0 / 159
    return optimizedConv2D(image, gaussianBlurKernel)

def motionBlur(image):
    motionBlurKernel = np.array([
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1]
    ]) * 1.0 / 9
    return optimizedConv2D(image, motionBlurKernel)

switcher = {
    'simple': simpleBlur,
    'more': blurMore,
    'average': averageBlur,
    'gaussian': gaussianBlur,
    'motion': motionBlur
}