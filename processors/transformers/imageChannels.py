import numpy as np

"""
    Defining channels transformations
"""

def blueChannel(pixel):
    return (pixel[0], 0, 0)

def greenChannel(pixel):
    return (0, pixel[1], 0)

def redChannel(pixel):
    return (0, 0, pixel[2])

def redBlueChannel(pixel):
    return (pixel[0], 0, pixel[2])

def redGreenChannel(pixel):
    return (0, pixel[1], pixel[2])

def greenBlueChannel(pixel):
    return (pixel[0], pixel[1], 0)

def toChannel(bmp, channel, half=False):
    """
        Keeping only channel(s) given using methods defined above

        Parameters
        ----------
        bmp: BMP

        channel: str | list

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
            if (channel == 'blue'):
                newImage[i][j] = blueChannel(newImage[i][j])
            elif (channel == 'green'):
                newImage[i][j] = greenChannel(newImage[i][j])
            elif (channel == 'red'):
                newImage[i][j] = redChannel(newImage[i][j])
            elif ('red' in channel and 'blue' in channel):
                newImage[i][j] = redBlueChannel(newImage[i][j])
            elif ('red' in channel and 'green' in channel):
                newImage[i][j] = redGreenChannel(newImage[i][j])
            elif ('green' in channel and 'blue' in channel):
                newImage[i][j] = greenBlueChannel(newImage[i][j])
    return newImage