#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from utils import helpers as hp

def printPixel(bmp, width, height):
    fullWidth = int(hp.readLittleEndian(bmp.width))
    fullHeight = int(hp.readLittleEndian(bmp.height))

    if height < fullHeight and width < fullWidth:
        print(bmp.imageData[height][width])
    else:
        print('ERR: The size of the file is {}x{}. Please provide numbers in those values'.format(fullWidth, fullHeight), file=sys.stderr)
        sys.exit(-1)