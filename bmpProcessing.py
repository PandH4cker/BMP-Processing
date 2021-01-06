#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys
from utils import helpers as hp
from processors.printHeader import printHeader
from processors.printPixel import printPixel
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
    elif len([x for x in (args.rotate, args.output) if x is not None]) == 1:
        parser.error('--rotate and --output mus be given together')
    elif len([x for x in (args.rotate, args.output) if x is not None]) == 2:
        pass #TODO
    else:
        printHeader(bmp)

if __name__ == '__main__':
    process_bmp()
    sys.exit(0)