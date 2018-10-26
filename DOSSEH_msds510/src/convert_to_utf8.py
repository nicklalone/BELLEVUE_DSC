import sys

def main(input_file_path, output_file_path):
    with open(input_file_path, encoding='ISO-8859-1') as f:
        text = f.read()

    with open(output_file_path, 'w', encoding='UTF8') as f:
        f.write(text)

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('usage: convert_to_utf8 ,<input_file>,<output_file>')
    else:
        main(str(args[1]), str(args[2]))


