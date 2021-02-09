import numpy as np
from utils import colourers

def gaussianKernel(size, sigma=1):
    colourers.info(f'Creating gaussian kernel of size {size} with sigma of {sigma}')
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g = np.exp(-((x**2 + y**2) / (2.0 * sigma ** 2))) * normal
    return g

def gaborKernel(size, sigma=8.0, theta=np.pi/4, lam=10.0, gamma=0.5, psi=3):
    sigmaX = sigma
    sigmaY = float(sigma) / gamma

    xmax = max(abs(size * sigmaX * np.cos(theta)), abs(size * sigmaY * np.sin(theta)))
    xmax = np.ceil(max(1, xmax))

    ymax = max(abs(size * sigmaX * np.sin(theta)), abs(size * sigmaY * np.cos(theta)))
    ymax = np.ceil(max(1, ymax))

    xmin = -xmax
    ymin = -ymax

    (y, x) = np.meshgrid(np.arange(ymin, ymax + 1), np.arange(xmin, xmax + 1))

    xTheta = x * np.cos(theta) + y * np.sin(theta)
    yTheta = -x * np.sin(theta) + y * np.cos(theta)

    gb = np.exp(-.5 * (xTheta ** 2 / sigmaX ** 2 + yTheta ** 2 / sigmaY ** 2)) * np.cos(2 * np.pi / lam * xTheta + psi)
    colourers.info(f'Creating gabor kernel of size {gb.shape[0]} with sigma of {sigma}')
    return gb