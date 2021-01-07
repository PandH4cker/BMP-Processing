import os, numpy as np
from utils import helpers as hp

class PNG:
    filename = ""
    ID = 0
    signature = ""
    mandatoryBytes = 0
    chunks = {}

    def __init__(self, filename:str):
        f = open(filename, 'rb')
        octets = []
        i = 1
        while (i <= 8):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1
        
        ID = [octets[0]]
        signature = [octets[1], octets[2], octets[3]]
        mandatoryBytes = [octets[4], octets[5], octets[6], octets[7]]

        self.filename = filename
        self.ID = ID
        self.signature = signature


        print('ID=', hex(self.ID[0])[2:].upper())

        for i in range(len(self.signature)):
            print(chr(self.signature[i]), " dec=", self.signature[i], "hexa=", hex(self.signature[i])[2:].upper())

        print(' '.join(hp.byteToHex(x) for x in mandatoryBytes))
        print('\t\t\t=>Magic Number =',self.signature)

        
        i = 1
        while (i <= 4):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1
        
        chunk1DataSize = [octets[8], octets[9], octets[10], octets[11]]
        print(' '.join(hp.byteToHex(x) for x in chunk1DataSize),
              '\t\t=>Taille chunk 1 = {} octets'.format(hp.readLittleEndian(chunk1DataSize)))

        i = 1
        while (i <= 4):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1

        chunkType = [octets[12], octets[13], octets[14], octets[15]]
        print(' '.join(hp.byteToHex(x) for x in chunkType),
              '\t\t=>Chunk Type = {}'.format(''.join(chr(x) for x in chunkType)))
        
        i = 1
        while (i <= 4):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1

        width = [octets[16], octets[17], octets[18], octets[19]]
        print(' '.join(hp.byteToHex(x) for x in width),
              '\t\t=>Width = {}'.format(int(hp.readLittleEndian(width))//256))
        
        i = 1
        while (i <= 4):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1

        height = [octets[20], octets[21], octets[22], octets[23]]
        print(' '.join(hp.byteToHex(x) for x in height),
              '\t\t=>Height = {}'.format(int(hp.readLittleEndian(height))//256))

        octets.append(ord(f.read(1)))

        bitDepth = [octets[24]]
        print(' '.join(hp.byteToHex(x) for x in bitDepth),
              '\t\t\t=>Bit Depth = {}'.format(hp.readLittleEndian(bitDepth)))

        octets.append(ord(f.read(1)))

        colorType = [octets[25]]
        print(' '.join(hp.byteToHex(x) for x in colorType),
              '\t\t\t=>Color Type = {}'.format(hp.readLittleEndian(colorType)))

        octets.append(ord(f.read(1)))

        compressionType = [octets[26]]
        print(' '.join(hp.byteToHex(x) for x in compressionType),
              '\t\t\t=>Compression Type = {}'.format(hp.readLittleEndian(compressionType)))

        octets.append(ord(f.read(1)))

        filterType = [octets[27]]
        print(' '.join(hp.byteToHex(x) for x in filterType),
              '\t\t\t=>Filter Type = {}'.format(hp.readLittleEndian(filterType)))

        octets.append(ord(f.read(1)))

        interlaceType = [octets[28]]
        print(' '.join(hp.byteToHex(x) for x in interlaceType),
              '\t\t\t=>Interlace Type = {}'.format(hp.readLittleEndian(interlaceType)))
        
        i = 1
        while (i <= 4):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1
        
        crc = [octets[29], octets[30], octets[31], octets[32]]
        print(' '.join(hp.byteToHex(x) for x in crc),
              '\t\t=>CRC = {}'.format(hp.readLittleEndian(crc)))

        i = 1
        while (i <= 4):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1
        
        chunk2DataSize = [octets[33], octets[34], octets[35], octets[36]]
        print(' '.join(hp.byteToHex(x) for x in chunk2DataSize),
              '\t\t=>Taille chunk 2 = {} octets'.format(hp.readLittleEndian(chunk2DataSize)))

        i = 1
        while (i <= 4):
            octet = f.read(1)
            octets.append(ord(octet))
            i += 1

        chunkType2 = [octets[37], octets[38], octets[39], octets[40]]
        print(' '.join(hp.byteToHex(x) for x in chunkType2),
              '\t\t=>Chunk Type = {}'.format(''.join(chr(x) for x in chunkType2)))


        f.close()