<<<<<<< HEAD
import sys

#create function to read avengers file and convert to UTF8 script
#output to interim data directory
def main(input_file_path, output_file_path):
    with open(input_file_path, encoding='ISO-8859-1 ') as f:
        text = f.read()

    with open(output_file_path, 'w', encoding='UTF8') as f:
        f.write(text)

#create funtion to read from command lines
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('usage: convert_to_utf8 <input_file> <output_file>')
    else:
        main(str(args[1]), str(args[2]))
=======
import sys

#create function to read avengers file and convert to UTF8 script
#output to interim data directory
def main(input_file_path, output_file_path):
    # I'm a big fan of variable names vs letters - names make code readable - e.g., csv_file and csv_file_utf8
    with open(input_file_path, encoding='ISO-8859-1 ') as f:
        text = f.read()

    with open(output_file_path, 'w', encoding='UTF8') as f:
        f.write(text)

#create funtion to read from command lines
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('usage: convert_to_utf8 <input_file> <output_file>')
    else:
        main(str(args[1]), str(args[2]))
>>>>>>> 8d9c3c470b3ce5d4b6c1970f922593046371fe98
