import sys


def  convert(inputfile, outputfile):

    '''
    Function to convert data in csv file encoded in 'ISO-8859-1' to 'utf-8' and save in another csv
    Arguments: 3 -  python code file, source file with path and  target file with path
    return: none
    Execution:  python convert_to_utf8.py ../data/raw/marvel-wikia-data.csv ../data/interim/marvel-wikia-data_utf8.csv
    '''

    in_avengers = open(inputfile, encoding='iso-8859-1')
    in_data = in_avengers.read()
    out_data = in_data.encode('utf8')

    out_avengers = open(outputfile, 'wb')
    out_avengers.write(out_data)

    in_avengers.close()
    out_avengers.close()

    print('File converted with utf-8 encoding and saved in interim directory')


def main():

    '''
    main function to call the convert function
    :return: none
    '''

    if (len(sys.argv)) < 3:
        print('Expecting 3 arguments - python filename, source file with path, target file with path')
    else:
        convert(sys.argv[1], sys.argv[2])


if __name__  == "__main__":

    main()
