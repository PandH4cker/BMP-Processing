from numpy.fft import fft, ifft, fft2, ifft2, fftshift, ifftshift, rfft2, irfft2
import numpy as np

def conv2D(image, kernel, half=False):
    """
        Apply a naive convolution between an image and a kernel

        Parameters
        ----------
        image: ndarray((h, w, 3))

        kernel: ndarray((h, w))

        half: Boolean - False by default, defining if we have to take only the half of the image

        Returns
        ------
        ndarray((h, w, 3))
    """
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

def optimizedConv2D(image, kernel):
    """
        Apply an optimized convolution between the image and the kernel

        Parameters
        ----------
        image: ndarray((h, w, 3))
        
        kernel: ndarray((h, w))

        Returns
        ------
        ndarray((h, w, 3))
    """

    image = image.astype(np.float16)
    kernelRowLength = len(kernel)
    halfkernelRowLength = kernelRowLength // 2
    flattenedKernel = kernel.flatten()
    numberOfCopies = len(flattenedKernel)
    copies = np.array([image.copy() for _ in range(numberOfCopies)])
    for i in range(numberOfCopies):
        currentLine = i // kernelRowLength
        currentColumn = i % kernelRowLength

        copies[i] = np.roll(copies[i], 
                            (
                                currentLine - halfkernelRowLength, 
                                currentColumn - halfkernelRowLength
                            ), 
                            axis=(0, 1)) * flattenedKernel[i]
    return np.sum(copies, axis=0)