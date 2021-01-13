import numpy as np

def average(pixel):
    return (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])/2

def imageGrayscale(bmp):
    """
        Applying grayscale to the image by using average with luminosity method

        Parameters
        ----------
        bmp: BMP

        Returns
        -------
        np.ndarray((h, w, 3))
    """
    for i in range(len(bmp.imageData)):
        for j in range(len(bmp.imageData[0])):
            bmp.imageData[i][j] = average(bmp.imageData[i][j])

    return np.clip(bmp.imageData, 0, 255).astype(float)