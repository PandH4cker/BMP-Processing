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
    width = len(bmp.imageData[0])
    if half:
        width = int(width/2)
    for i in range(len(bmp.imageData)):
        for j in range(width):
            bmp.imageData[i][j] = invert(bmp.imageData[i][j])
    
    return bmp.imageData