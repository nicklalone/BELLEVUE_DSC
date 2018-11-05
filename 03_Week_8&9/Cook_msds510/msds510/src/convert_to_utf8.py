import sys

# The following code opens up the file

'''
This portion of the code reads the input file using ISO-8859-1 and stores it into the variable text
The variable text is then used to write the file to the designated output file. The output file is
written with UTF-8 encoding.
'''
def main(input_file_path, output_file_path):
    with open(input_file_path, encoding='ISO-8859-1 ') as f:
        text = f.read()

#  The following code takes in the destination path filename and creates a new file

    with open(output_file_path, 'w', encoding='UTF8') as f:
        f.write(text)

# The following code will make sure that a source and destination file path is given and if not it prints amessage to enter

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('usage: convert_to_utf8 <input_file> <output_file>')
    else:
        main(str(args[1]), str(args[2]))

