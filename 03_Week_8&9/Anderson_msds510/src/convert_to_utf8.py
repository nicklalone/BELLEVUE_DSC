"""
I think as we are new to github (at least I know I am) we all forgot that we should comment our code to make it easy for a third party to read
Here for example, I would include a comment such as :
Create function to open file and convert it to UTF-8
Simple, but I think it will be definitively helpful to the next person that will takeover this code.
"""

import sys

# The following code opens up the input file
# Read command reads all the contents of the file

def main(input_file_path, output_file_path):
    with open(input_file_path, encoding='ISO-8859-1 ') as f:
        text = f.read()

# The following code opens up the file in  the write mode

    with open(output_file_path, 'w', encoding='UTF8') as f:
        f.write(text)

# The following code checks if there are 3 arguments given in the commandline

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('usage: convert_to_utf8 <input_file> <output_file>')
    else:
        main(str(args[1]), str(args[2]))
            #testing
