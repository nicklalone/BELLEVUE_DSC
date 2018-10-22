import sys
import csv

try:
    input_file = sys.argv[1]
except IndexError as err_log:
    print('Error:', err_log)
    print('Requires 1 input for the input file.')
    sys.exit()


def reading(input):
    with open(input, 'r') as f:
        temp_file = csv.DictReader(f)
        output_file = []
        for row in temp_file:
            output_file.append(row)
        print(output_file[160])


if __name__ == '__main__':
    reading(input_file)