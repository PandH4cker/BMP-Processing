import numpy as np

def imageBinary(bmp, half=False):
    """
        Applying binary mask to the image by checking, 
        if the color is inferior to 128 (half of 256) we assign black color,
        else we assign white color.

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
            if all(i <= 128 for i in newImage[i][j]):
                newImage[i][j] = (0, 0, 0)
            else:
               newImage[i][j] = (255, 255, 255)
    
    return newImage