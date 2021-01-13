#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from utils import helpers as hp

def imageRotate(bmp, degree):
    """
        Rotating the image using np.rot90 and 
        specifying the number of times to do the operation

        Parameters
        ----------
        bmp: BMP

        degree: [90, 180, 270]

        Returns
        -------
        np.ndarray((h, w, 3))
    """
    return np.rot90(bmp.imageData, k=int(degree/90)).astype(float)