import os, numpy as np
from utils import helpers as hp

class BMP:
    filename = ""
    signature = ""
    totalSize = 0
    appImage = ""
    startingOffset = 0
    headerSize = 0
    width = 0
    height = 0
    planes = 0
    bpp = 0
    compressionType = 0
    imageSize = 0
    hRes = 0
    vRes = 0
    numberOfColors = 0
    numberOfImportantColors = 0
    imageData = 0

    def __init__(self, filename:str):
        f = open(filename, 'rb')
        octets = []
        i = 1
        while (i <= 54):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1
        
        signature = [octets[0], octets[1]]
        totalSize = [octets[2], octets[3], octets[4], octets[5]]
        appImage = [octets[6], octets[7], octets[8], octets[9]]
        startingOffset = [octets[10], octets[11], octets[12], octets[13]]
        headerSize = [octets[14], octets[15], octets[16], octets[17]]
        width = [octets[18], octets[19], octets[20], octets[21]]
        height = [octets[22], octets[23], octets[24], octets[25]]
        planes = [octets[26], octets[27]]
        bpp = [octets[28], octets[29]]
        compressionType = [octets[30], octets[31], octets[32], octets[33]]
        imageSize = [octets[34], octets[35], octets[36], octets[37]]
        hRes = [octets[38], octets[39], octets[40], octets[41]]
        vRes = [octets[42], octets[43], octets[44], octets[45]]
        numberOfColors = [octets[46], octets[47], octets[48], octets[49]]
        numberOfImportantColors = [octets[50], octets[51], octets[52], octets[53]]

        self.filename = filename
        self.signature = signature
        self.totalSize = totalSize
        self.appImage = appImage
        self.startingOffset = startingOffset
        self.headerSize = headerSize
        self.width = width
        self.height = height
        self.planes = planes
        self.bpp = bpp
        self.compressionType = compressionType
        self.imageSize = imageSize
        self.hRes = hRes
        self.vRes = vRes
        self.numberOfColors = numberOfColors
        self.numberOfImportantColors = numberOfImportantColors

        height = int(hp.readLittleEndian(self.height))
        width = int(hp.readLittleEndian(self.width))
        
        self.imageData = np.zeros((height, width, 3))
        for i in  range(height):
            for j in range(width):
                self.imageData[i][j] = (ord(f.read(1)), ord(f.read(1)), ord(f.read(1)))
        
        f.close()