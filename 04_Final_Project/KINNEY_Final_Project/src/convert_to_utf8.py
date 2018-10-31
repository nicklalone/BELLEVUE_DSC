"""
2. Convert to UTF8 Script
python convert_to_utf8.py ../data/raw/sourcefile.csv ../data/interim/sourcefile_utf8.csv
"""

import sys


def convert_to_utf(infile, outfile):
    try:
        _infile = open(infile,  encoding='iso-8859-1')
        indata = _infile.read() # reading content in 'iso-8859-1' format
        _outfile = open(outfile, 'wb')
        _outfile.write(indata.encode('utf8')) # Writing in 'utf-8' format
    except Exception as e:
        print(e)

    _infile.close()
    _outfile.close() # Closing the file
    print('File {0} created with utf-8 encoded data'.format(sys.argv[2]))
    return


def main():
    convert_to_utf(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
