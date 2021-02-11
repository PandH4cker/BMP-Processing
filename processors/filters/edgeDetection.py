import numpy as np
from utils import colourers, conv2D, optimizedConv2D, gaussianKernel

def sobelFilters(image):
    """
        Apply Sobel filters in X and Y directions

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    colourers.info(f'Applying Sobel filter in X and Y directions')
    Kx = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], np.float32)
    Ky = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ], np.float32)
    
    Ix = optimizedConv2D(image, Kx)
    Iy = optimizedConv2D(image, Ky)

    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)

    return (G, theta)

def prewittFilters(image):
    """
        Apply Prewitt filters in X and Y directions

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    colourers.info(f'Applying Prewitt filter in X and Y directions')
    Kx = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ], np.float32)
    Ky = np.array([
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1]
    ], np.float32)
    
    Ix = optimizedConv2D(image, Kx)
    Iy = optimizedConv2D(image, Ky)

    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)

    return (G, theta)

def robertsFilters(image):
    """
        Apply Roberts filters in X and Y directions

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    colourers.info(f'Applying Roberts filter in X and Y directions')
    Kx = np.array([
        [1,  0],
        [0, -1]
    ], np.float32)
    Ky = np.array([
        [ 0, 1],
        [-1, 0]
    ], np.float32)
    
    Ix = optimizedConv2D(image, Kx)
    Iy = optimizedConv2D(image, Ky)

    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)

    return (G, theta)

def kirschFilters(image):
    """
        Apply Kirsch filters in X and Y directions

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    colourers.info(f'Applying Kirsch filter in X and Y directions')
    Kx = np.array([
        [-3, -3, 5],
        [-3,  0, 5],
        [-3, -3, 5]
    ], np.float32)
    Ky = np.array([
        [-3, -3, -3],
        [-3,  0, -3],
        [ 5,  5,  5]
    ], np.float32)
    
    Ix = optimizedConv2D(image, Kx)
    Iy = optimizedConv2D(image, Ky)

    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    theta = np.arctan2(Iy, Ix)

    return (G, theta)

def nonMaxSuppression(image, D):
    """
        Remove irrelevant pixels using the matrix of angles

        Parameters
        ----------
        image: ndarray((h, w, 3))
        D: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """

    colourers.info(f'Removing non maxima pixels using gradient directions matrix')
    M, N, dim = image.shape
    Z = np.zeros((M, N, dim), dtype=np.int32)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    for i in range(1, M-1):
        for j in range(1, N-1):
            try:
                q = 255
                r = 255

                # angle 0
                if all(
                    np.logical_or(
                        [all(0 <= angle[i, j]), all(angle[i, j] < 22.5)], 
                        [all(157.5 <= angle[i, j]), all(angle[i, j] <= 180)]
                    )
                ):
                    q = image[i, j+1]
                    r = image[i, j-1]
                # angle 45
                elif all((22.5 <= angle[i, j] < 67.5)):
                    q = image[i+1, j-1]
                    r = image[i-1, j+1]
                # angle 90
                elif all((67.5 <= angle[i, j] < 112.5)):
                    q = image[i+1, j]
                    r = image[i-1, j]
                # angle 135
                elif all((112.5 <= angle[i, j] < 157.5)):
                    q = image[i-1, j-1]
                    r = image[i+1, j+1]
                
                if all(
                    np.logical_and(
                        (image[i, j] >= q),
                        (image[i, j] >= r)
                    )
                ):
                    Z[i, j] = image[i, j]
                else:
                    Z[i, j] = 0, 0, 0

            except IndexError as e:
                pass
    return Z

def threshold(image, lowThresholdRatio=0.05, highThresholdRatio=0.09, weakPix=25, strongPix=255):
    """
        Double thresholding the image by using the low and high threshold 
        and the weak and strong pixel values.

        Parameters
        ----------
        image: ndarray((h, w, 3))

        lowThresholdRatio: float

        highThresholdRatio: float

        weakPix: int

        strongPix: int

        Returns
        -------
        ndarray((h, w, 3))
    """

    colourers.info(f'Performing double threshold to detect weak and strong pixels with a threshold of {lowThresholdRatio}-{highThresholdRatio}')
    highThreshold = image.max() * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio

    M, N, dim = image.shape
    res = np.zeros((M, N, dim), dtype=np.int32)

    weak = np.int32(weakPix)
    strong = np.int32(strongPix)

    iStrong, jStrong, _ = np.where(image >= highThreshold)
    iZeros, jZeros, _ = np.where(image < lowThreshold)

    iWeak, jWeak, _ = np.where((image <= highThreshold) & (image >= lowThreshold))

    res[iStrong, jStrong] = strong, strong, strong
    res[iWeak, jWeak] = weak, weak, weak

    return res

def hysteresis(image, weakPixel, strongPixel):
    """
        Applying hysteresis for reducing errors and sharpening edges.

        Parameters
        ----------
        image: ndarray((h, w, 3))

        weakPixel: int

        strongPixel: int

        Returns
        -------
        ndarray((h, w, 3))
    """
    colourers.info(f'Performing hysteresis using weak pixel of {weakPixel} and strong pixel of {strongPixel}')
    M, N, dim = image.shape
    weak = weakPixel
    strong = strongPixel

    for i in range(1, M-1):
        for j in range(1, N-1):
            if all(image[i, j] == weak):
                try:
                    if all(
                        np.logical_or(
                            np.logical_or(
                                np.logical_or(
                                    (image[i+1, j-1] == strong),
                                    (image[i+1, j] == strong)
                                ),
                                np.logical_or(
                                    (image[i+1, j+1] == strong),
                                    (image[i, j-1] == strong)
                                )
                            ),
                            np.logical_or(
                                np.logical_or(
                                    (image[i, j+1] == strong),
                                    (image[i-1, j-1] == strong)
                                ),
                                np.logical_or(
                                    (image[i-1, j] == strong),
                                    (image[i-1, j+1] == strong)
                                )
                            )
                        )
                    ):
                        image[i, j] = strong, strong, strong
                    else:
                        image[i, j] = 0, 0, 0
                except IndexError as e:
                    pass
    return image

def cannyEdgeDetection(image, sigma=1, kernelSize=5, weakPix=75, strongPix=255, lowThreshold=0.05, highThreshold=0.15):
    """
        Apply the Canny filter for an edge detection

        Parameters
        ----------
        image: ndarray((h, w, 3))

        sigma: float

        kernelSize: int

        weakPix: int

        strongPix: int

        lowThreshold: int

        highThreshold: int

        Returns
        -------
        ndarray((h, w, 3))
    """

    smoothedImage = optimizedConv2D(image, gaussianKernel(kernelSize, sigma))
    gradientMatrix, thetaMatrix = sobelFilters(smoothedImage)
    nonMaxImage = nonMaxSuppression(gradientMatrix, thetaMatrix)
    thresholdImage = threshold(nonMaxImage, lowThresholdRatio=lowThreshold, highThresholdRatio=highThreshold, weakPix=weakPix, strongPix=strongPix)
    return hysteresis(thresholdImage, weakPixel=weakPix, strongPixel=strongPix)

def sobelEdgeDetection(image, sigma=1, kernelSize=5):
    """
        Apply the Sobel filter for an edge detection

        Parameters
        ----------
        image: ndarray((h, w, 3))

        sigma: float

        kernelSize: int

        Returns
        -------
        ndarray((h, w, 3))
    """

    smoothedImage = optimizedConv2D(image, gaussianKernel(kernelSize, sigma))
    gradientMatrix, thetaMatrix = sobelFilters(smoothedImage)
    return gradientMatrix

def prewittEdgeDetection(image, sigma=1, kernelSize=5):
    """
        Apply the Prewitt filter for an edge detection

        Parameters
        ----------
        image: ndarray((h, w, 3))

        sigma: float

        kernelSize: int

        Returns
        -------
        ndarray((h, w, 3))
    """

    smoothedImage = optimizedConv2D(image, gaussianKernel(kernelSize, sigma))
    gradientMatrix, thetaMatrix = prewittFilters(smoothedImage)
    return gradientMatrix

def robertsEdgeDetection(image, sigma=1, kernelSize=5):
    """
        Apply the Roberts filter for an edge detection

        Parameters
        ----------
        image: ndarray((h, w, 3))

        sigma: float

        kernelSize: int

        Returns
        -------
        ndarray((h, w, 3))
    """

    smoothedImage = optimizedConv2D(image, gaussianKernel(kernelSize, sigma))
    gradientMatrix, thetaMatrix = robertsFilters(smoothedImage)
    return gradientMatrix

def kirschEdgeDetection(image, sigma=1, kernelSize=5):
    """
        Apply the Kirsch filter for an edge detection

        Parameters
        ----------
        image: ndarray((h, w, 3))

        sigma: float

        kernelSize: int

        Returns
        -------
        ndarray((h, w, 3))
    """

    smoothedImage = optimizedConv2D(image, gaussianKernel(kernelSize, sigma))
    gradientMatrix, thetaMatrix = kirschFilters(smoothedImage)
    return gradientMatrix