import sys
import csv

# Method to make python friendly user names once extracted
def python_friendly_name(name):
    return name.lower().replace(' ', '_').replace('/', '_').replace('?', '')


def main(input_csv, output_csv):
    with open(input_csv) as f:
        csv_reader = csv.DictReader(f)
        records = [record for record in csv_reader]
        fieldnames = csv_reader.fieldnames

# A method to take the path for the input and the output file
# Dict Reader Object was generated and iterated to get all the rows
# We can operate on the DictReader object and extract the fieldnames
# The file default is opened in the read mode

    python_friendly_names = [python_friendly_name(name) for name in fieldnames]
    new_records = [{python_friendly_name(name): value for name, value in record.items()} for record in records]

# The following code opens the output file in the write mode
# When Dict writer was used we need to specify the field names

    with open(output_csv, 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=python_friendly_names)
        csv_writer.writeheader()
        csv_writer.writerows(new_records)

# The following code checks the if the relevant number of arguements were specified in the commandline
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print('usage: write_csv <input_csv> <output_csv>')
    else:
        main(args[1], args[2])

