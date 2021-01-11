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

# [ 255. 255. 255. ]
def npToArray(ndarray):
    """
        Convert numpy array to bytearray

        Parameters
        ----------
        ndarray: np.ndarray

        Return
        ------
        bytearray
    """

    octets = []
    for i in range(len(ndarray)):
        octets.append(int(ndarray[i]))
    return bytearray(octets)

def saveBMP(bmp, imageData, outputFile):
    """
        Save matrix of a BMP to a bmp file by rewriting the header (v3).

        Parameters
        ----------
        bmp: BMP

        imageData: np.ndarray((h, w, 3))

        outputFile: str
    """
    f = open(outputFile, 'wb')

    signature = bytearray(bmp.signature)
    f.write(signature)

    totalSize = len(imageData[0]) * len(imageData) * 3 + 54
    totalSize = totalSize.to_bytes(4, byteorder='little')
    f.write(totalSize)

    appImage = bytearray(bmp.appImage)
    f.write(appImage)

    startingOffset = bytearray(bmp.startingOffset)
    f.write(startingOffset)

    headerSize = bytearray(bmp.headerSize)
    f.write(headerSize)

    width = len(imageData[0]).to_bytes(4, byteorder='little')
    f.write(width)
    
    height = len(imageData).to_bytes(4, byteorder='little')
    f.write(height)

    planes = bytearray(bmp.planes)
    f.write(planes)

    bpp = bytearray(bmp.bpp)
    f.write(bpp)

    compressionType = bytearray(bmp.compressionType)
    f.write(compressionType)

    imageSize = len(imageData[0]) * len(imageData) * 3
    imageSize = imageSize.to_bytes(4, byteorder='little')
    f.write(imageSize)

    hRes = bytearray(bmp.hRes)
    f.write(hRes)

    vRes = bytearray(bmp.vRes)
    f.write(vRes)

    numberOfColors = bytearray(bmp.numberOfColors)
    f.write(numberOfColors)

    numberOfImportantColors = bytearray(bmp.numberOfImportantColors)
    f.write(numberOfImportantColors)

    height = len(imageData)
    width = len(imageData[0])

    for i in range(height):
        for j in range(width):
            f.write(npToArray(imageData[i][j]))

    f.close()

def atLeastOne(filterVar, filterList):
    """
        Check if one of the filterList is set and if filterVar is set.

        Parameters
        ----------
        filterVar: any

        filterList: list

        Returns
        -------
        bool
    """
    
    return len(
        list(
            filter(lambda x: x != False and x != None , [x and filterVar for x in filterList])
            )
        ) > 0