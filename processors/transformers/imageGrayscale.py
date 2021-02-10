import numpy as np

def averageLuminosity(pixel):
    return (0.114 * pixel[0] + 0.587 * pixel[1] + 0.299 * pixel[2])/2

def imageGrayscale(bmp, half=False):
    """
        Applying grayscale to the image by using average with luminosity method

        Parameters
        ----------
        bmp: BMP

        Returns
        -------
        np.ndarray((h, w, 3))
    """
    newImage = bmp.imageData.copy()
    width = len(newImage[0])
    if half:
        width = int(width/2)
    for i in range(len(newImage)):
        for j in range(width):
            newImage[i][j] = averageLuminosity(newImage[i][j])

    return np.clip(newImage, 0, 255).astype(float)