import numpy as np
from numpy.fft import fft2, ifft2
from utils import colourers

def wienerFilter(image, kernel, K):
    kernel /= np.sum(kernel)
    newImage = image.copy()
    newImage = fft2(newImage)
    kernel = fft2(kernel, s=(image.shape[0], image.shape[1]))
    kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
    newImage[:,:,0] = newImage[:,:,0] * kernel
    newImage[:,:,1] = newImage[:,:,1] * kernel
    newImage[:,:,2] = newImage[:,:,2] * kernel
    newImage = np.abs(ifft2(newImage))
    minval = np.percentile(newImage, 2)
    maxval = np.percentile(newImage, 98)
    newImage = np.clip(newImage, minval, maxval)
    newImage = ((newImage - minval) / (maxval - minval)) * 255
    return newImage.astype(np.uint8)