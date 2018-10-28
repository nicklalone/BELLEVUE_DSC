# Converts the passed in file to UTF-8 by simply
# opening it as UTF-8 and saving it. The path
# must be passed in as part of the args.
import sys

def main(input_file, output_file):
    # We haven't gone into exception handling, but it's really necessary here
    try:
        with open(input_file, encoding = 'ISO-8859-1') as file:
            file_text = file.read()
            file.close()

        with open(output_file, 'w', encoding = 'UTF8') as file:
            file.write(file_text)
            file.close()
    except:
        print('An exception occurred:', sys.exc_info())

# This gets executed first
if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print('Note usage: convert_to_utf8.py <input_file>, <output_file>')
    else:
        main(sys.argv[1], sys.argv[2])
