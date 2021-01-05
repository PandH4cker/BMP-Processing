#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys

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

def ouverture_Fichiers_Image(filename):
    """Read BMP Image and print header infos
    
    Parameters
    ----------
    filename: str

    """

    f_lecture =open(filename,'rb') #read in binary mode
    i=1
    octet = bytes([0])
    octets=[]
    #Lecture du MAGIC NUMBER
    while (i <= 2): #lecture Magic number sur 2 octets
        octet=f_lecture.read(1) #Lecture octet par octet
        octets.append(ord(octet))
        print (octet.decode('utf-8')," dec=",ord(octet), "hexa=",hex(ord(octet))[2:].upper())
        i=i+1
    print("\t\t\t=>Magic Number =", octets, " BM => BitMap")
    #BLOC ENTETE 54 octets en standard
    while (i<=54):
        octet=f_lecture.read(1)
        octets.append(ord(octet))
        i=i+1

    # Taille du fichier
    size = [octets[2], octets[3], octets[4], octets[5]]
    print(' '.join(byteToHex(x) for x in size), 
          '\t\t=>taille de Fichier = {} octets'.format(readLittleEndian(size)))
    print(size, '\t=>taille de Fichier = {} octets'.format(readLittleEndian(size)))

    # Application Image
    appImage = [octets[6], octets[7], octets[8], octets[9]]
    print(' '.join(byteToHex(x) for x in appImage),
          '\t\t=>application image = {} noms'.format(readLittleEndian(appImage)))

    # Taille Entete
    headerSize = [octets[10], octets[11], octets[12], octets[13]]
    print(' '.join(byteToHex(x) for x in headerSize),
          '\t\t=>Taille Entete = {} octets'.format(readLittleEndian(headerSize)))

    # Largeur Image
    width = [octets[18], octets[19], octets[20], octets[21]]
    print(' '.join(byteToHex(x) for x in width),
          '\t\t=>Largeur Image = {} pixels'.format(readLittleEndian(width)))

    # Hauteur Image
    height = [octets[22], octets[23], octets[24], octets[25]]
    print(' '.join(byteToHex(x) for x in height),
          '\t\t=>Hauteur Image = {} pixels'.format(readLittleEndian(height)))

    # Plans d'image
    planes = [octets[26], octets[27]]
    print(' '.join(byteToHex(x) for x in planes),
          '\t\t\t=>NB plan Image = {} plan'.format(readLittleEndian(planes)))

    # Couleurs Image
    colors = [octets[28], octets[29]]
    print(' '.join(byteToHex(x) for x in colors),
          '\t\t\t=>NB Couleur Image = {} couleurs'.format(readLittleEndian(colors)))
          
    f_lecture.close

def process_bmp():
    """Process a given BMP Image in parameter

    """

    # Parsing des arguments
    parser = argparse.ArgumentParser(description='BMP reader')
    parser.add_argument('--bmp', 
                        metavar='<bmp file name', 
                        help='image file to parse', 
                        default='image.bmp', 
                        required=True)
    args = parser.parse_args()
    file_name = args.bmp
    if not os.path.isfile(file_name):
        print('"{}" does not exist'.format(file_name), file=sys.stderr)
        sys.exit(-1)
    print('Success Opening {}...'.format(file_name))
    ouverture_Fichiers_Image(file_name)


if __name__ == '__main__':
    process_bmp()
    sys.exit(0)