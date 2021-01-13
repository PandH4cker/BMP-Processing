import numpy as np

def imageContrast(bmp, factor):
    """
        Applying image contrast by using the formula: 
        128 + factor * matrix - factor * 128

        Parameters
        ----------
        bmp: BMP

        factor: float

        Returns
        -------
        np.ndarray((h, w, 3))
    """

    return np.clip(128 + float(factor) * bmp.imageData - float(factor) * 128.0, 0, 255).astype(float)