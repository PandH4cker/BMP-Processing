#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import helpers as hp

def printHeader(bmp):
      for i in range(len(bmp.signature)):
            print(chr(bmp.signature[i]), " dec=", bmp.signature[i], "hexa=", hex(bmp.signature[i])[2:].upper())

      print("\t\t\t=>Magic Number =", bmp.signature, 
      " BM => BitMap Windows,\n\t\t\t\t\t\t  "
      " BA => BitMap OS2,\n\t\t\t\t\t\t ",
      " CI => Icone couleur OS2,\n\t\t\t\t\t\t ",
      " CP => Pointeur de couleur OS2,\n\t\t\t\t\t\t ",
      " IC => Icone OS2,\n\t\t\t\t\t\t ",
      " PT => Pointeur OS2")

      # Taille du fichier
      print(' '.join(hp.byteToHex(x) for x in bmp.totalSize), 
            '\t\t=>Taille total du Fichier = {} octets'.format(hp.readLittleEndian(bmp.totalSize)))
      print(bmp.totalSize, '\t\t=>Taille total du Fichier = {} octets'.format(hp.readLittleEndian(bmp.totalSize)))

      # Application Image
      print(' '.join(hp.byteToHex(x) for x in bmp.appImage),
            '\t\t=>Application Image = {} noms'.format(hp.readLittleEndian(bmp.appImage)))

      # Offset du début de l'image
      print(' '.join(hp.byteToHex(x) for x in bmp.startingOffset),
            '\t\t=>Offset du début de l\'image = {} octets'.format(hp.readLittleEndian(bmp.startingOffset)))

      # Taille Entete
      print(' '.join(hp.byteToHex(x) for x in bmp.headerSize),
            '\t\t=>Taille Entete = {} octets'.format(hp.readLittleEndian(bmp.headerSize)))

      # Largeur Image
      print(' '.join(hp.byteToHex(x) for x in bmp.width),
            '\t\t=>Largeur Image = {} pixels'.format(hp.readLittleEndian(bmp.width)))

      # Hauteur Image
      print(' '.join(hp.byteToHex(x) for x in bmp.height),
            '\t\t=>Hauteur Image = {} pixels'.format(hp.readLittleEndian(bmp.height)))

      # Plans d'image
      print(' '.join(hp.byteToHex(x) for x in bmp.planes),
            '\t\t\t=>NB plan Image = {} plan'.format(hp.readLittleEndian(bmp.planes)))

      # BPP
      print(' '.join(hp.byteToHex(x) for x in bmp.bpp),
            '\t\t\t=>BPP (bit par pixel) = {} bpp'.format(hp.readLittleEndian(bmp.bpp)))

      # Type de compression
      print(' '.join(hp.byteToHex(x) for x in bmp.compressionType),
            '\t\t=>Type de compression (0=Aucune, 1=RLE-8, 2=RLE-4) = {}'.format(hp.readLittleEndian(bmp.compressionType)))

      # Taille avec padding
      print(' '.join(hp.byteToHex(x) for x in bmp.imageSize),
            '\t\t=>Taille de l\'image = {} octets'.format(hp.readLittleEndian(bmp.imageSize)))


      # Résolution Horizontale
      print(' '.join(hp.byteToHex(x) for x in bmp.hRes),
            '\t\t=>Résolution horizontale = {} pixels/m'.format(hp.readLittleEndian(bmp.hRes)))

      # Résolution Verticale
      print(' '.join(hp.byteToHex(x) for x in bmp.vRes),
            '\t\t=>Résolution verticale = {} pixels/m'.format(hp.readLittleEndian(bmp.vRes)))

      # Nombre de couleurs dans l'image
      print(' '.join(hp.byteToHex(x) for x in bmp.numberOfColors),
            '\t\t=>NB couleur Image = {} couleurs'.format(hp.readLittleEndian(bmp.numberOfColors)))

      # Nombre de couleurs dans l'image
      print(' '.join(hp.byteToHex(x) for x in bmp.numberOfImportantColors),
            '\t\t=>NB couleur importante Image = {} couleurs'.format(hp.readLittleEndian(bmp.numberOfImportantColors)))