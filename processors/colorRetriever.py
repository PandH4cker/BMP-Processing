import numpy as np

def toRGB(image):
    w, h, dim = image.shape
    ret = np.empty((w, h, dim), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            ret[i][j] = image[i][j][0], image[i][j][1], image[i][j][2]
    return ret