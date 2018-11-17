"""
Convert to UTF8 Script
Implement the convert_to_utf8.py script and generate a csv file in the interim data directory.
This script should take two command line arguments, an input file and the output file. After you have finished
implementing the script, you should be able to run the script as follows.

python convert_to_utf8.py ../data/raw/inputfile.csv ../data/interim/inputfile_utf8.csv
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
    print('File {0} created with utf-8 encoded data and written to the interim folder.'.format(outfile))
    return


def main():
    convert_to_utf(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
