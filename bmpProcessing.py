#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys
from utils import helpers as hp, colourers
from processors import imageBinary, imageChannels, imageContrast, imageGrayscale, printHistogram
from processors import imageInvert, imageRotate, imageScale, printHeader, printPixel, toChannel
from middlewares.length import required_length
from formats.bmp import BMP
from formats.png import PNG
import colorama

colorama.init(autoreset=True)

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
    group.add_argument('--histogram',
                       action='store_true',
                       help='print histogram associated')
    group.add_argument('--output',
                        '-o',
                        type=str,
                        metavar='<output file>',
                        help='image output file')


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
    parser.add_argument('--invert',
                        '-i',
                        action='store_true',
                        help='to inverted image, equivalent to --contrast -1')
    parser.add_argument('--channel',
                        type=str,
                        choices=['blue', 'green', 'red'],
                        metavar='<channel>',
                        nargs='+',
                        action=required_length(1, 2),
                        help='to the specified channel')

    args = parser.parse_args()

    filename = ""
    if args.bmp:
        filename = args.bmp

        if not os.path.isfile(filename):
            colourers.error('"{}" does not exist !'.format(filename))
            sys.exit(-1)
        colourers.success('Success Opening {}...'.format(filename))

        bmp = BMP(filename)

        if args.print_color:
            width, height = args.print_color
            colourers.info(f'Printing pixel color of ({width}, {height})')
            printPixel(bmp, width, height)
            sys.exit(0)
        
        elif args.header:
            colourers.info(f'Printing BMP header of {bmp.filename}')
            printHeader(bmp)
            sys.exit(0)
        
        elif args.histogram:
            colourers.info(f'Printing color histogram of {bmp.filename}')
            printHistogram(bmp)
            sys.exit(0)
        
        if (args.rotate or args.scale or args.contrast or args.grayscale or args.binary or args.channel):
            if not hp.atLeastOne(args.output, (
                args.rotate,
                args.scale,
                args.contrast,
                args.grayscale,
                args.binary,
                args.channel
            )):
                parser.error('--rotate/--scale/--contrast/--grayscale/--binary and --output must be given together')
        
        if args.rotate:
            degree = args.rotate
            colourers.info(f'Rotating image to {degree} degree')
            bmp.imageData = imageRotate(bmp, degree)

        if args.scale:
            if len(args.scale) == 2:
                width, height = args.scale
                colourers.info(f'Scaling image to {width}x{height} pixels')
                bmp.imageData = imageScale(bmp, height, width)
            else:
                scaleRatio = args.scale[0]

                colourers.info(f'Scaling image to {scaleRatio} scale ratio')

                height = int(hp.readLittleEndian(bmp.height))
                width = int(hp.readLittleEndian(bmp.width))

                bmp.imageData = imageScale(bmp, height * scaleRatio, width * scaleRatio)
        
        if args.contrast:
            factor = args.contrast
            colourers.info(f'Applying a factor contrast of {factor}')
            bmp.imageData = imageContrast(bmp, factor)
        
        if args.grayscale:
            colourers.info(f'Applying grayscale mask to the image')
            bmp.imageData = imageGrayscale(bmp)
        
        if args.binary:
            colourers.info(f'Applying binary mask to the image')
            bmp.imageData = imageBinary(bmp)
        
        if args.invert:
            colourers.info(f'Inverting image colours')
            bmp.imageData = imageInvert(bmp)
        
        if args.channel:
            if len(args.channel) == 2:
                c1, c2 = args.channel
                colourers.info(f'Keeping only {c1} and {c2} channels of the image')
                bmp.imageData = toChannel(bmp, [c1, c2])
            else:
                channel = args.channel[0]
                colourers.info(f'Keeping only {channel} channel of the image')
                bmp.imageData = toChannel(bmp, channel)

        if args.output:
            outputFile = args.output
            hp.saveBMP(bmp, bmp.imageData, outputFile)
            colourers.success(f'Succesfully saved into {outputFile}')
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