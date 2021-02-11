import numpy as np
from processors.transformers.imageScale import scale

def overlap(image, overlappers):
    """
        Performing an overlapping between multiple images

        Parameters
        ----------
        image: ndarray((h, w, 3))

        overlappers: list(ndarray((h, w, 3)))

        Returns
        -------
        ndarray((h, w, 3))
    """

    M, N, dim = image.shape
    for img in overlappers:
        if (img.shape != image.shape):
            img = np.array(scale(img, M, N))
        image = np.minimum(image, img)
    return image