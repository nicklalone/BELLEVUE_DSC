import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]


def make_nice_name(name):
    new_name = []
    for x in name:
        temp_name = x.lower().replace(' ', '_').replace('/', '_').strip('?').strip('\n')
        new_name.append(temp_name)
    return new_name


def reading(input):
    with open(input, 'r') as f:
        temp_file = csv.DictReader(f)
        temp_file.fieldnames = make_nice_name(temp_file.fieldnames)
        output_file = []
        for row in temp_file:
            output_file.append(row)
        return temp_file.fieldnames, output_file


def writer(input, output, header):
    with open(output, 'w', newline='') as o:
        output_writer = csv.DictWriter(o, fieldnames=header)
        output_header = {}
        # Want a row of the header;
        for x in header:
            output_header[x] = x
        output_writer.writerow(output_header)
        for row in input:
            output_writer.writerow(row)


if __name__ == '__main__':
    temp_csv = reading(input_file)
    writer(temp_csv[1], output_file, temp_csv[0])
