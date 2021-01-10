from matplotlib import pyplot as plt
import numpy as np

def printHistogram(bmp):
    plt.title('Histogram for given image')
    plt.xlabel('Value')
    plt.ylabel('Pixels Frequency')
    plt.hist(bmp.imageData[:, :, 0])
    plt.show()