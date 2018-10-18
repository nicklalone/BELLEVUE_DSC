import sys
import os

def argumentexists (index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

def conversion (input, output):
    avengers = open(input, 'rb')
    avengersdecoded = avengers.read()
    avengersdecoded = avengersdecoded.decode('ISO-8859-1')
    writeAvengers = open(output, 'w')
    writeAvengers.write(avengersdecoded)
    writeAvengers.close()


if __name__ == '__main__':
    targetFile = argumentexists(1)
    returnFile = argumentexists(2)
    if targetFile and returnFile:
        conversion(targetFile, returnFile)
