import numpy as np

def invert(pixel):
    return (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])

def imageInvert(bmp, half=False):
    """
        Inverting pixels by doing 255 - pixel

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
            newImage[i][j] = invert(newImage[i][j])
    
    return newImage