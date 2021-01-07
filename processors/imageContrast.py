import numpy as np

def imageContrast(bmp, factor):
    return np.clip(128 + float(factor) * bmp.imageData - float(factor) * 128.0, 0, 255).astype(float)