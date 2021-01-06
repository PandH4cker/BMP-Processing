#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np, os
from utils import helpers as hp

def imageRotate(bmp, degree, outputFile):
    rotatedImage = np.rot90(bmp.imageData)
    f = open(outputFile, 'wb')

    signature = bytearray(bmp.signature)
    f.write(signature)

    totalSize = bytearray(bmp.totalSize)
    f.write(totalSize)

    appImage = bytearray(bmp.appImage)
    f.write(appImage)

    startingOffset = bytearray(bmp.startingOffset)
    f.write(startingOffset)

    headerSize = bytearray(bmp.headerSize)
    f.write(headerSize)

    width = bytearray(bmp.width)
    f.write(width)

    height = bytearray(bmp.height)
    f.write(height)

    planes = bytearray(bmp.planes)
    f.write(planes)

    bpp = bytearray(bmp.bpp)
    f.write(bpp)

    compressionType = bytearray(bmp.compressionType)
    f.write(compressionType)

    imageSize = bytearray(bmp.imageSize)
    f.write(imageSize)

    hRes = bytearray(bmp.hRes)
    f.write(hRes)

    vRes = bytearray(bmp.vRes)
    f.write(vRes)

    numberOfColors = bytearray(bmp.numberOfColors)
    f.write(numberOfColors)

    numberOfImportantColors = bytearray(bmp.numberOfImportantColors)
    f.write(numberOfImportantColors)

    height = int(hp.readLittleEndian(bmp.height))
    width = int(hp.readLittleEndian(bmp.width))

    for i in range(height):
        for j in range(width):
            f.write(hp.npToArray(rotatedImage[i][j]))

    f.close()
