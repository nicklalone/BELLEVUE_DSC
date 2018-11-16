import csv
import sys

# For this recordset, it makes no sense to have a separate file for one line of code.
def format_header(name):
    return name.lower().replace(' ', '_').replace('/', '_').replace('?', '')

def read_write_csv_dict(input_file, output_file):
    try:
        with open(input_file) as file:
            csv_reader = csv.DictReader(file)
            fieldnames = csv_reader.fieldnames
            records = [row for row in csv_reader]

        formatted_headers = [format_header(name) for name in fieldnames]
        new_records = [{format_header(name): value for name, value in record.items()} for record in records]

        print("Printing headers and rows...")
        print(new_records)

        # Save the file
        with open(output_file, 'w') as f:
            csv_writer = csv.DictWriter(f, fieldnames=formatted_headers)
            csv_writer.writeheader()
            csv_writer.writerows(new_records)
    except:
        print('An exception occurred:', sys.exc_info())

