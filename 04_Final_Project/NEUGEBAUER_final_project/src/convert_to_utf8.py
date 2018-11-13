# Converts the passed in file to UTF-8 by simply
# opening it as UTF-8 and saving it. Don't want
# to use the command line, opting for a YAML
# config setup instead.
import sys
import yaml

def main(input_file, output_file):
    # We haven't gone into exception handling, but it's really necessary here
    try:
        with open(input_file, encoding = 'ISO-8859-1') as file:
            file_text = file.read()
            print("Read the raw .csv file", input_file)
            file.close()

        with open(output_file, 'w', encoding = 'UTF8') as file:
            file.write(file_text)
            print('Writing the UTF8 file output to ', output_file)
            file.close()
    except:
        print('An exception occurred:', sys.exc_info())

# This gets executed
'''
    The YAML setup was extremely simple. The code here and in 
    ../config/config.yml is self explanatory, noting that the
    format for the .yml file in this case is simply a key/value
    pair separated by a colon ':'. 
'''
if __name__ == "__main__":
    config = yaml.safe_load(open('../config/config.yml'))
    print('Opened YAML config')

    inputFileName = config.get('RawInputFile')
    print('Got the input file name.', inputFileName)

    interimUTF8Name = config.get('InterimUTF8File')
    print('Got the output file name', interimUTF8Name)

    main(inputFileName, interimUTF8Name)


