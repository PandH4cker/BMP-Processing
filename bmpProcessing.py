#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys, numpy as np, colorama
from utils import helpers as hp, colourers
from processors import imageBinary, imageChannels, imageContrast, imageGrayscale, printHistogram
from processors import imageInvert, imageRotate, imageScale, printHeader, printPixel, toChannel
from processors import cannyEdgeDetection
from middlewares.length import required_length
from formats.bmp import BMP
from formats.png import PNG

# Initialization of colorama
colorama.init(autoreset=True)

def imageProcessing():
    """
        Process a given image in parameter (BMP or PNG)
    """

    # Parser initialization
    parser = argparse.ArgumentParser(description=colourers.toCyan('Image processor for reading/writing images into BMP/PNG formats and applying transformations on it.'))
    
    # Formats Parser
    group = parser.add_argument_group(colourers.toGreen('formats'))
    formatParser = group.add_mutually_exclusive_group(required=True)
    formatParser.add_argument('--bmp',
                               type=str,
                               metavar=colourers.toRed('<bmp file name>'), 
                               help=colourers.toMagenta('bmp file to parse'))
    formatParser.add_argument('--png',
                              type=str,
                              metavar=colourers.toRed('<png file name>'),
                              help=colourers.toMagenta('png file to parse'))

    # Printers Parser
    group = parser.add_argument_group(colourers.toYellow('printers'))
    printers = group.add_mutually_exclusive_group()
    printers.add_argument('--header',
                       help=colourers.toMagenta('print the file format header'),
                       action='store_true')
    printers.add_argument('--print-color',
                       '-pc',
                       type=int,
                       nargs=2,
                       metavar=(colourers.toRed('<width>'), colourers.toRed('<height>')),
                       help=colourers.toMagenta('pixel to print'))
    printers.add_argument('--histogram',
                       action='store_true',
                       help=colourers.toMagenta('print histogram associated'))
    printers.add_argument('--output',
                        '-o',
                        type=str,
                        metavar=colourers.toRed('<output file>'),
                        help=colourers.toMagenta('image output file'))

    # Transformers Parser
    transformers = parser.add_argument_group(colourers.toBlue('transformers'))
    transformers.add_argument('--rotate',
                        '-r',
                        type=int,
                        choices=[90, 180, 270],
                        metavar=colourers.toRed('<degree of rotation>'),
                        help=colourers.toMagenta('rotate the image'))
    transformers.add_argument('--scale',
                        '-s',
                        type=int,
                        nargs='+',
                        action=required_length(1, 2),
                        metavar=(colourers.toRed('<scaleRatio> | [<width>'), colourers.toRed('<height>')),
                        help=colourers.toMagenta('scale/shrink the image'))
    transformers.add_argument('--contrast',
                        '-c',
                        type=float,
                        metavar=colourers.toRed('<contrast factor>'),
                        help=colourers.toMagenta('apply a factor contrast'))
    transformers.add_argument('--grayscale',
                        '-gs',
                        action='store_true',
                        help=colourers.toMagenta('to grayscale image'))
    transformers.add_argument('--binary',
                        '-b',
                        action='store_true',
                        help=colourers.toMagenta('to binary image'))
    transformers.add_argument('--invert',
                        '-i',
                        action='store_true',
                        help=colourers.toMagenta('to inverted image, equivalent to --contrast -1'))
    transformers.add_argument('--channel',
                        type=str,
                        choices=['blue', 'green', 'red'],
                        metavar=colourers.toRed('<channel>'),
                        nargs='+',
                        action=required_length(1, 2),
                        help=colourers.toMagenta('to the specified channel'))
    
    filters = parser.add_argument_group(colourers.toCyan('filters'))
    filters.add_argument('--edge-detection',
                         '-ed',
                         action='store_true',
                         help=colourers.toMagenta('perform edge detection'))

    # Args parsing
    args = parser.parse_args()

    filename = ""
    # BMP Block
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
        
        if (args.rotate or args.scale or args.contrast or args.grayscale or 
            args.binary or args.channel or args.edge_detection):
            if not hp.atLeastOne(args.output, (
                args.rotate,
                args.scale,
                args.contrast,
                args.grayscale,
                args.binary,
                args.channel,
                args.edge_detection
            )):
                parser.error('--rotate/--scale/--contrast/--grayscale/--binary/--channel/--edge-detection and --output must be given together')
        
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
        
        if args.edge_detection:
            colourers.info(f'Performing edge detection')
            bmp.imageData = cannyEdgeDetection(bmp.imageData, sigma=0.33, kernelSize=5, 
                                               lowThreshold=0.09, highThreshold=0.17, weakPix=100)

        if args.output:
            outputFile = args.output
            hp.saveBMP(bmp, bmp.imageData, outputFile)
            colourers.success(f'Succesfully saved into {outputFile}')
            sys.exit(0)
        
        parser.error('Give at least one more argument')
        
    # PNG Block
    else:
        filename = args.png

        if not os.path.isfile(filename):
            print('"{}" does not exist'.format(filename), file=sys.stderr)
            sys.exit(-1)
        print('Success Opening {}...'.format(filename))
        
        png = PNG(filename)

# Main function
if __name__ == '__main__':
    imageProcessing()
    sys.exit(0)