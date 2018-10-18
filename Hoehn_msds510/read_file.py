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
    curr = os.getcwd()
    print (curr)
    os.chdir(input)
    new = os.getcwd()
    print(new)


if __name__ == '__main__':
    targetFile = argumentexists(1)
    returnFile = argumentexists(2)
    if targetFile and returnFile:
        conversion(targetFile, returnFile)
