import sys, csv
#from msds510.utils import cleaners

def main():
    """
    :args: an array with input and output files
    :result: executes csvCleaner process
    """
    if len(sys.argv) != 3:
        print('This cleaner takes two arguments: <input file> <output file>')
    else:
        csvCleaner(sys.argv[1], sys.argv[2])
        print('Cleaned from {} to {}')#.format(str(sys.argv[1]), str(sys.argv[2]))

def csvCleaner(input, output):
    """

    :param input: this is the location of the input file to be cleaned
    :param output: this is the location of the cleaned output file
    :return: a file with pythonized fieldnames and entries
    """
    file = []
    fieldnames = []
    with open(input, 'rU') as f:
        reader = csv.DictReader(f, delimiter = ',')
        file = list(reader)
    #for key in file[0]
     #   print(file[0][key])
      #  print(file[0])
    print(file[0])



if __name__ == '__main__':
    main()
