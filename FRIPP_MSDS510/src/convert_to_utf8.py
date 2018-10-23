import sys
"""
Converts a ISO-8859-1 encoded csv to UTF8 encoding
"""
def main():

    #rb is for 'read binary' to read in lines from file for conversion
    with open(sys.argv[1],'rb') as f:
        lines = f.read()
    decodedData = lines.decode('ISO-8859-1')

    #write the decoded data as new file
    with open(sys.argv[2],'w') as n:
        n.write(decodedData)

#identify file as 'main'
if __name__ == '__main__':
    main()
