from matplotlib import pyplot as plt
import numpy as np

def printHistogram(bmp):
    """
        Print the histogram of colors of the bmp file using Matplotlib

        Parameters
        ----------
        bmp: BMP
    """
    flattenedImage = bmp.imageData[:, :, :].flatten()
    blueFlattened = bmp.imageData[:, :, 0].flatten()
    greenFlattened = bmp.imageData[:, :, 1].flatten()
    redFlattened = bmp.imageData[:, :, 2].flatten()

    figure, axes = plt.subplots()
    axes.hist(flattenedImage, bins=256, color='cyan', alpha=0.3)

    if not (blueFlattened.all() == greenFlattened.all() == redFlattened.all()):
        axes.hist(blueFlattened, bins=256, color='blue', alpha=0.5)
        axes.hist(greenFlattened, bins=256, color='green', alpha=0.5)
        axes.hist(redFlattened, bins=256, color='red', alpha=0.5)
        axes.set_title(f'Color channel Histogram for given image {bmp.filename}')
        plt.legend(['Total of Channels', 'Blue Channel', 'Green Channel', 'Red Channel'])
    else:
        axes.hist(redFlattened, bins=256, color='gray', alpha=0.5)
        axes.set_title(f'Histogram of the grayscale image {bmp.filename}')
        plt.legend(['Total of Channels', 'Grayscale'])

    axes.set_xlabel('Value')
    axes.set_ylabel('Pixels Frequency')
    plt.show()