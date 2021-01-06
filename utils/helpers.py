#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def byteToHex(b):
    """Convert byte to Hex in readable format
    
    Parameters
    ----------
    b: Bytes

    Return
    ------
    str

    """

    return str(hex(b)[2:]).zfill(2).upper()

def readLittleEndian(l):
    """Read from bytes in little endian
    
    Parameters
    ----------
    l: list[Bytes]

    Return
    ------
    str

    """

    return str(int.from_bytes(l, byteorder='little'))

def npToArray(ndarray):
    octets = []
    for i in range(len(ndarray)):
        octets.append(int(ndarray[i]))
    return bytearray(octets)

def saveBMP(bmp, imageData, outputFile):
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

    height = int(readLittleEndian(bmp.height))
    width = int(readLittleEndian(bmp.width))

    for i in range(height):
        for j in range(width):
            f.write(npToArray(imageData[i][j]))

    f.close()