#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys
from utils import helpers as hp
from processors.printHeader import printHeader
from processors.printPixel import printPixel
from processors.imageRotate import imageRotate
from processors.imageScale import imageScale
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
                       help='print the BMP Header',
                       action='store_true')
    group.add_argument('--print-color',
                       '-pc',
                       type=int,
                       nargs=2,
                       metavar=('<width>', '<height>'),
                       help='pixel to print')
    group.add_argument('--rotate',
                       '-r',
                       type=int,
                       choices=[90, 180, 270],
                       metavar='<degree of rotation>',
                       help='rotate the image')
    group.add_argument('--scale',
                       '-s',
                       type=int,
                       nargs='+',
                       action=required_length(1, 2),
                       metavar=('<scaleRatio> | [<width>', '<height>'),
                       help='scale/shrink the image')

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
        
        elif args.header:
            printHeader(bmp)

        elif (
            len([x for x in (args.rotate, args.output) if x is not None]) in (0, 1) and
            len([x for x in (args.scale, args.output) if x is not None]) in (0, 1)
        ):
            parser.error('--rotate/--scale and --output must be given together')

        elif len([x for x in (args.rotate, args.output) if x is not None]) == 2:
            degree = args.rotate
            outputFile = args.output
            imageRotate(bmp, degree, outputFile)

        elif len([x for x in (args.scale, args.output) if x is not None]) == 2:
            if len(args.scale) == 2:
                width, height = args.scale
                outputFile = args.output
                imageScale(bmp, height, width, outputFile)
            else:
                scaleRatio = args.scale[0]
                outputFile = args.output

                height = int(hp.readLittleEndian(bmp.height))
                width = int(hp.readLittleEndian(bmp.width))

                imageScale(bmp, height * scaleRatio, width * scaleRatio, outputFile)
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