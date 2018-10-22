import sys
import csv

try:
    input_file = sys.argv[1]
except IndexError as err_log:
    print('Error:', err_log)
    print('Requires 1 argument: an input file')
    sys.exit()

output_file = []


def reading(input):
    with open(input, 'r') as f:
        temp_file = csv.reader(f)
        for row in temp_file:
            output_file.append(row)
        print(output_file[161])


if __name__ == '__main__':
    reading(input_file)