import numpy as np

def conv2D(image, kernel, half=False):
    s = image.shape
    py = int((kernel.shape[0] - 1)/2)
    px = int((kernel.shape[1] - 1)/2)
    newImage = image.copy()
    if half:
        imax = int(s[1]/2)
    else:
        imax = s[1] - px
    for i in range(px, imax):
        for j in range(py, s[0] - py):
            it = 0.0
            for k in range(-px, px+1):
                for l in range(-py, py+1):
                    it += image[j + 1][i + k] * kernel[l + py][k + px]
            newImage[j][i] = it
    return np.clip(newImage, 0, 255).astype(float)