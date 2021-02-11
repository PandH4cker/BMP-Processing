import numpy as np

def fakingColors(pixel):
    """
        Faking colors on the image by trying to reverse the grayscale implementation

        Parameters
        ----------
        pixel: tuple(B, G, R)

        Returns
        -------
        tuple(B, G, R)
    """

    return (
        pixel[0] * 0.598 - 0.1957 * pixel[1] - 0.038 * pixel[2],
        pixel[1] * 1.174 - pixel[0] * 0.1994 - pixel[2] * 0.076,
        pixel[2] * 0.228 - pixel[0] * 0.1495 - pixel[1] * 0.2935
    )

def retrieveColor(image):
    """
        Try retrieving colors of the grayscale image

        Parameters
        ----------
        image: ndarray((h, w, 3))

        Returns
        -------
        ndarray((h, w, 3))
    """
    w, h, dim = image.shape
    ret = np.zeros((w, h, dim), dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            ret[i][j] = fakingColors(image[i][j])
    return np.clip(ret, 0, 255)