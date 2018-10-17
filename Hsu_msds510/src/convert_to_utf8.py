import sys

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except IndexError as err_log:
    print('Error:', err_log)
    print('Requires 2 arguments: 1st is input file, 2nd is output file.')
    sys.exit()


def convert(input, output):
    with open(input, 'rb') as f:
        lines = f.read()
    decode_data = lines.decode('ISO-8859-1')
    with open(output, 'w') as g:
        g.write(decode_data)


if __name__ == '__main__':
    convert(input_file, output_file)