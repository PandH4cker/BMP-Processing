#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import helpers as hp

def scale(image, nR, nC):
    nR0 = len(image)
    nC0 = len(image[0])
    return [
        [
            image[int(nR0 * r / nR)][int(nC0 * c / nC)] for c in range(nC)
        ] for r in range(nR)
    ]

def imageScale(bmp, nR, nC, outputFile):
    scaledImage = scale(bmp.imageData, nR, nC)
    hp.saveBMP(bmp, scaledImage, outputFile)