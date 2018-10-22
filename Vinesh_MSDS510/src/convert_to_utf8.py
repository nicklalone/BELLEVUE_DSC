import sys
"""
This module helps to convert a ISO-8859-1 encoded csv to UTF8 encoded csv file.
command line argument 1 is file name which needs to be converted
command line argument 2 is UTF8 encoded file name which will be created
"""
def main():

    with open(sys.argv[1],'rb') as f:
        lines = f.read()
    decodedData = lines.decode('ISO-8859-1')
    with open(sys.argv[2],'w') as e:
        e.write(decodedData)

if __name__ == '__main__':
    main()
