#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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