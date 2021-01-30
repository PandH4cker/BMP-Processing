import numpy as np
from processors.transformers.imageScale import scale

def overlap(image, overlappers):
    M, N, dim = image.shape
    for img in overlappers:
        if (img.shape != image.shape):
            img = np.array(scale(img, M, N))
        image = np.minimum(image, img)
    return image