#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys
from utils import helpers as hp
from processors.printHeader import printHeader
from processors.printPixel import printPixel
from processors.imageRotate import imageRotate
from processors.imageScale import imageScale
from processors.imageContrast import imageContrast
from processors.imageGrayscale import imageGrayscale
from processors.imageBinary import imageBinary
from middlewares.length import required_length
from formats.bmp import BMP
from formats.png import PNG

def process_bmp():
    """Process a given BMP Image in parameter

    """

    # Parsing des arguments
    parser = argparse.ArgumentParser(description='BMP reader')

    formatParser = parser.add_mutually_exclusive_group(required=True)
    formatParser.add_argument('--bmp',
                               type=str,
                               metavar='<bmp file name>', 
                               help='image file to parse')
    formatParser.add_argument('--png',
                              type=str,
                              metavar='<png file name>',
                              help='image file to parse')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--header',
                       help='print the file format header',
                       action='store_true')
    group.add_argument('--print-color',
                       '-pc',
                       type=int,
                       nargs=2,
                       metavar=('<width>', '<height>'),
                       help='pixel to print')

    parser.add_argument('--rotate',
                        '-r',
                        type=int,
                        choices=[90, 180, 270],
                        metavar='<degree of rotation>',
                        help='rotate the image')
    parser.add_argument('--scale',
                        '-s',
                        type=int,
                        nargs='+',
                        action=required_length(1, 2),
                        metavar=('<scaleRatio> | [<width>', '<height>'),
                        help='scale/shrink the image')
    parser.add_argument('--contrast',
                        '-c',
                        type=float,
                        metavar='<contrast factor>',
                        help='apply a factor contrast')
    parser.add_argument('--grayscale',
                        '-gs',
                        action='store_true',
                        help='to grayscale image')
    parser.add_argument('--binary',
                        '-b',
                        action='store_true',
                        help='to binary image')
    parser.add_argument('--output',
                        '-o',
                        type=str,
                        metavar='<output file>',
                        help='image output file')

    args = parser.parse_args()

    filename = ""
    if args.bmp:
        filename = args.bmp

        if not os.path.isfile(filename):
            print('"{}" does not exist'.format(filename), file=sys.stderr)
            sys.exit(-1)
        print('Success Opening {}...'.format(filename))

        bmp = BMP(filename)

        if args.print_color:
            width, height = args.print_color
            printPixel(bmp, width, height)
            sys.exit(0)
        
        elif args.header:
            printHeader(bmp)
            sys.exit(0)
        
        if (args.rotate or args.scale or args.contrast or args.grayscale):
            if not hp.atLeastOne(args.output, (
                args.rotate,
                args.scale,
                args.contrast,
                args.grayscale,
                args.binary
            )):
                parser.error('--rotate/--scale/--contrast/--grayscale/--binary and --output must be given together')
        
        if args.rotate:
            degree = args.rotate
            bmp.imageData = imageRotate(bmp, degree)

        if args.scale:
            if len(args.scale) == 2:
                width, height = args.scale
                bmp.imageData = imageScale(bmp, height, width)
            else:
                scaleRatio = args.scale[0]

                height = int(hp.readLittleEndian(bmp.height))
                width = int(hp.readLittleEndian(bmp.width))

                bmp.imageData = imageScale(bmp, height * scaleRatio, width * scaleRatio)
        
        if args.contrast:
            factor = args.contrast
            bmp.imageData = imageContrast(bmp, factor)
        
        if args.grayscale:
            bmp.imageData = imageGrayscale(bmp)
        
        if args.binary:
            bmp.imageData = imageBinary(bmp)

        if args.output:
            outputFile = args.output
            hp.saveBMP(bmp, bmp.imageData, outputFile)
            sys.exit(0)
        
        parser.error('Give at least one more argument')
    else:
        filename = args.png

        if not os.path.isfile(filename):
            print('"{}" does not exist'.format(filename), file=sys.stderr)
            sys.exit(-1)
        print('Success Opening {}...'.format(filename))
        
        png = PNG(filename)

if __name__ == '__main__':
    process_bmp()
    sys.exit(0)