#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys
from utils import helpers as hp
from processors.printHeader import printHeader
from processors.printPixel import printPixel
from processors.imageRotate import imageRotate
from processors.imageScale import imageScale
from middlewares.length import required_length
from bmp import BMP

def process_bmp():
    """Process a given BMP Image in parameter

    """

    # Parsing des arguments
    parser = argparse.ArgumentParser(description='BMP reader')
    parser.add_argument('--bmp',
                        type=str,
                        metavar='<bmp file name>', 
                        help='image file to parse', 
                        default='image.bmp', 
                        required=True)

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
    file_name = args.bmp

    if not os.path.isfile(file_name):
        print('"{}" does not exist'.format(file_name), file=sys.stderr)
        sys.exit(-1)
    print('Success Opening {}...'.format(file_name))

    bmp = BMP(file_name)

    if args.print_color:
        width, height = args.print_color
        printPixel(bmp, width, height)

    elif (
        len([x for x in (args.rotate, args.output) if x is not None]) == 1 and
        len([x for x in (args.scale, args.output) if x is not None]) == 1
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
        printHeader(bmp)

if __name__ == '__main__':
    process_bmp()
    sys.exit(0)