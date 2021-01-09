import numpy as np

def imageBinary(bmp):
    for i in range(len(bmp.imageData)):
        for j in range(len(bmp.imageData[0])):
            if all(i <= 128 for i in bmp.imageData[i][j]):
                bmp.imageData[i][j] = (0, 0, 0)
            else:
                bmp.imageData[i][j] = (255, 255, 255)
    
    return bmp.imageData