import os, numpy as np
from utils import helpers as hp

class BMP:
    """
        BMP model class defining the BMP structure and storing data from a BMP file.

        A BMP is a file which contains a signature that can be one of [BM, BA, CI, CP, IC, PT].

        It has a total size which is the 54 first bytes + the image data size.

        It can be referenced by an application image like Photoshop, Windows Paint or whatever.

        The starting offset defines where the image data starts. On a v3 it's at the 54-th bytes.

        The header size should be 40 bytes for a v3 but it can differ depending on which version of bmp is used.

        It has a width and a height and a number of planes.

        The bpp is the Bit per Pixel, it is very important for image reader to assign colors 
        to the image when reading the image data.

        The compression type can be 0=None, 1=RLE-8, 2=RLE-4.

        There is the image size which defines the size of the image data matrix.

        There are horizontal and vertical resolutions defined in pixels/meter.

        The number of colors and the number of important colors allow us to determine if a palette has been used.

        The image data is the matrix of pixels.
    """

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
        """
            Constructor of the BMP class. Read the first 54 bytes and assigns them to the variables.
            Then assigns the matrix with the bytes depending on the width and the height.
        """

        # Reading the first 54 bytes
        f = open(filename, 'rb')
        octets = []
        i = 1
        while (i <= 54):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1
        
        # Assigning the bytes
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
        
        # Assigning the matrix of pixels (Adding 3 bytes per iterations)
        self.imageData = np.zeros((height, width, 3))
        for i in  range(height):
            for j in range(width):
                self.imageData[i][j] = (ord(f.read(1)), ord(f.read(1)), ord(f.read(1)))
        
        f.close()