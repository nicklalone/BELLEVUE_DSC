import sys

def argumentExists(index): #function to try get arguments that will not crash program if argument out of bounds
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]

def conversion(input, output): #function to write out file.
    avengers = open(input,'rb')
    avengersdecoded = avengers.read()
    avengersdecoded = avengersdecoded.decode('ISO-8859-1')
    avengers.close()
    writeAvengers = open(output, 'w')
    writeAvengers.write(avengersdecoded)
    writeAvengers.close()

if __name__ == "__main__":
    targetFile = argumentExists(1)
    resultFile = argumentExists(2)
    if targetFile and resultFile: #both arguments have value
        conversion(targetFile, resultFile)

