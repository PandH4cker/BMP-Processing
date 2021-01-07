#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from utils import helpers as hp

def imageRotate(bmp, degree, outputFile):
    return np.rot90(bmp.imageData, k=int(degree/90))