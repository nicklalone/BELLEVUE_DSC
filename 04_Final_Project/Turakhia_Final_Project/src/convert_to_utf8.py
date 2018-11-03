import sys
import csv

def argumentExists(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

def conversion(input, output):
    biopics = open(input, 'rb')
    biopicsdecoded = biopics.read()
    biopicsdecoded = biopicsdecoded.decode('ISO-8859-1')
    biopics.close()
    writebiopics = open(output, 'w', encoding='UTF8')
    writebiopics.write(biopicsdecoded)
    writebiopics.close()

if __name__ == "__main__":
    targetFile = argumentExists(1)
    resultFile = argumentExists(2)
    if targetFile and resultFile:
        conversion(targetFile, resultFile)
