import os, sys, re

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from processors import printers as Printers, transformers as Transformers, filters as Filters
from utils import helpers as hp, colourers, gaussianKernel, gaborKernel
from formats import BMP, PNG

import shutil
shutil.rmtree('output', ignore_errors=True)
os.mkdir('output')

colourers.info('Using lena_couleur.bmp as a testing image')
filename = '../lena_couleur.bmp'

colourers.info('Creating the BMP class from filename')
bmp = BMP(filename)
colourers.success('Created BMP class successfully')

colourers.info('Header printing')
Printers.printHeader(bmp)
colourers.success('Header printed successfully')

colourers.info('Printing the color of the first pixel')
Printers.printPixel(bmp, 0, 0)
colourers.success('Successfully printed the color of the first pixel')

colourers.info('Printing the histogram of the image')
Printers.printHistogram(bmp)
colourers.success('Successfully printed the histogram')

colourers.info('Rotating the image (90, 180, 270)')
os.mkdir('output/rotate')
for degree in [90, 180, 270]:
    newImage = Transformers.rotate(bmp, degree)
    hp.saveBMP(bmp, newImage, outputFile='output/rotate/r-'+str(degree)+'.bmp')
colourers.success('Successfully rotated the image')

colourers.info('Scaling the image (by factor and with dims)')
os.mkdir('output/scale')

height = int(hp.readLittleEndian(bmp.height))
width = int(hp.readLittleEndian(bmp.width))
for ratio in [2, 3, 4]:
    newImage = Transformers.scale(bmp, height * ratio, width * ratio)
    hp.saveBMP(bmp, newImage, outputFile='output/scale/sf-'+str(ratio)+'.bmp')

newImage = Transformers.scale(bmp, 1080, 1920)
hp.saveBMP(bmp, newImage, outputFile='output/scale/s-1920-1080.bmp')
colourers.success('Successfully scaled the image')

colourers.info('Applying contrast on the image')
os.mkdir('output/contrast')
for factor in range(-5, 6):
    newImage = Transformers.contrast(bmp, factor)
    hp.saveBMP(bmp, newImage, outputFile=f'output/contrast/c-{factor}.bmp')
colourers.success('Successfully applied contrast on the image')

colourers.info('Applying grayscale on the image (and half image)')
os.mkdir('output/grayscale')
newImage = Transformers.grayscale(bmp)
hp.saveBMP(bmp, newImage, outputFile=f'output/grayscale/gs.bmp')
newImage = Transformers.grayscale(bmp, half=True)
hp.saveBMP(bmp, newImage, outputFile=f'output/grayscale/gs-half.bmp')
colourers.success('Successfully applied grayscale')

colourers.info('Applying binary mask to the image (and half image)')
os.mkdir('output/binary')
newImage = Transformers.binary(bmp)
hp.saveBMP(bmp, newImage, outputFile=f'output/binary/b.bmp')
newImage = Transformers.binary(bmp, half=True)
hp.saveBMP(bmp, newImage, outputFile=f'output/binary/b-half.bmp')
colourers.success('Successfully applied binary mask')

colourers.info('Inverting image colours')
os.mkdir('output/invert')
newImage = Transformers.invert(bmp)
hp.saveBMP(bmp, newImage, outputFile=f'output/invert/i.bmp')
newImage = Transformers.invert(bmp, half=True)
hp.saveBMP(bmp, newImage, outputFile=f'output/invert/i-half.bmp')
colourers.success('Successfully inverting image colours')

colourers.info('Keeping specific channels')
os.mkdir('output/channel')
for channels in [['red', 'green'], ['red', 'blue'], ['blue', 'green'], 'red', 'green', 'blue']:
    newImage = Transformers.toChannel(bmp, channels)
    if len(channels) == 2:
        hp.saveBMP(bmp, newImage, outputFile=f'output/channel/ch-{channels[0]}-{channels[1]}.bmp')
    else:
        hp.saveBMP(bmp, newImage, outputFile=f'output/channel/ch-{channels}.bmp')

    newImage = Transformers.toChannel(bmp, channels,  half=True)
    if len(channels) == 2:
        hp.saveBMP(bmp, newImage, outputFile=f'output/channel/ch-{channels[0]}-{channels[1]}-half.bmp')
    else:
        hp.saveBMP(bmp, newImage, outputFile=f'output/channel/ch-{channels}-half.bmp')
colourers.success('Successfully kept specific channels')

colourers.info('Denoising the image (Wiener Filter)')
os.mkdir('output/denoise')
newImage = Filters.wienerFilter(bmp.imageData, gaussianKernel(9, sigma=0.33), K=10)
hp.saveBMP(bmp, newImage, outputFile=f'output/denoise/d.bmp')
colourers.success('Successfully denoised the image')

colourers.info('Applying texture detection (Gabor Filter)')
os.mkdir('output/texture-detection')
newImage = Filters.gaborFilter(bmp.imageData, gaborKernel(0))
hp.saveBMP(bmp, newImage, outputFile=f'output/texture-detection/td.bmp')
colourers.success('Successfully detected the texure')

colourers.info('Applying increased edge enhancement filter')
os.mkdir('output/increased-edge-enhancement')
newImage = Filters.iee(bmp.imageData)
hp.saveBMP(bmp, newImage, outputFile=f'output/increased-edge-enhancement/iee.bmp')
colourers.success('Successfully increased edges')

colourers.info('Performing edge detection')
os.mkdir('output/edge-detection')
for filterName in ['canny', 'sobel', 'prewitt', 'roberts', 'kirsch']:
    if filterName == 'canny':
        newImage = Filters.ced(bmp.imageData, sigma=0.33, kernelSize=9, weakPix=50)
    elif filterName == 'sobel':
        newImage = Filters.sed(bmp.imageData,  sigma=0.33, kernelSize=9)
    elif filterName == 'prewitt':
        newImage = Filters.ped(bmp.imageData,  sigma=0.33, kernelSize=9)
    elif filterName == 'roberts':
        newImage = Filters.red(bmp.imageData,  sigma=0.33, kernelSize=9)
    elif filterName == 'kirsch':
        newImage = Filters.ked(bmp.imageData,  sigma=0.33, kernelSize=9)
    
    hp.saveBMP(bmp, newImage, outputFile=f'output/edge-detection/{filterName}.bmp')
colourers.success('Successfully performed edge detection')

colourers.info('Sharpening the image')
os.mkdir('output/sharpen')
newImage = Filters.sharpen(bmp.imageData)
hp.saveBMP(bmp, newImage, outputFile=f'output/sharpen/s.bmp')
colourers.success('Successfully sharpened the image')

colourers.info('Unsharpening the image')
os.mkdir('output/unsharp')
newImage = Filters.unsharp(bmp.imageData)
hp.saveBMP(bmp, newImage, outputFile=f'output/unsharp/u.bmp')
colourers.success('Successfully unsharped the image')

colourers.info('Retrieving color')
os.mkdir('output/retrieve-color')
newImage = Filters.retrieveColor(bmp.imageData)
hp.saveBMP(bmp, newImage, outputFile=f'output/retrieve-color/r.bmp')
colourers.success('Successfully retrieved colors')

colourers.info('Performing blur on the image (20 iterations)')
os.mkdir('output/blur')
for blurType in ['simple', 'more', 'gaussian', 'average', 'motion']:
    newImage = bmp.imageData
    for _ in range(20):
        blurFunc = Filters.blur.switcher.get(blurType)
        newImage = blurFunc(newImage)
    hp.saveBMP(bmp, newImage, outputFile=f'output/blur/{blurType}.bmp')
colourers.success('Successfully performed blur on the image')

colourers.info('Performing emboss filter')
os.mkdir('output/emboss')
newImage = Filters.emboss(bmp.imageData)
hp.saveBMP(bmp, newImage, outputFile=f'output/emboss/e.bmp')
colourers.success('Successfully performed emboss filter')

colourers.info('Performing an overlapping between multiple images')
os.mkdir('output/overlap')
paths = ['output/emboss/e.bmp', 'output/retrieve-color/r.bmp', 'output/texture-detection/td.bmp']
overlappers = []
for p in paths:
    overlappers.append(BMP(p).imageData)
newImage = Filters.overlap(bmp.imageData, overlappers)
hp.saveBMP(bmp, newImage, outputFile=f'output/overlap/o.bmp')
colourers.success('Successfully overlapped the images')
colourers.success('End of tests. Images will be in the output directory.')