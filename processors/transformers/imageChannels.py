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

def toChannel(bmp, channel):
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
    for i in range(len(bmp.imageData)):
        for j in range(len(bmp.imageData[0])):
            if (channel == 'blue'):
                bmp.imageData[i][j] = blueChannel(bmp.imageData[i][j])
            elif (channel == 'green'):
                bmp.imageData[i][j] = greenChannel(bmp.imageData[i][j])
            elif (channel == 'red'):
                bmp.imageData[i][j] = redChannel(bmp.imageData[i][j])
            elif ('red' in channel and 'blue' in channel):
                bmp.imageData[i][j] = redBlueChannel(bmp.imageData[i][j])
            elif ('red' in channel and 'green' in channel):
                bmp.imageData[i][j] = redGreenChannel(bmp.imageData[i][j])
            elif ('green' in channel and 'blue' in channel):
                bmp.imageData[i][j] = greenBlueChannel(bmp.imageData[i][j])

    return bmp.imageData