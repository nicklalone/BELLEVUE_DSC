import os
import re
import sys
from datetime import date


def get_filename_and_path(file_path):
    """
    To split folder path and file name from argument
    @param file_path:
    @return: file_name,folder_path
    """
    try:
        index = file_path.rindex("/")
        folder_path = file_path[0:index]
        file_name = file_path[index:]
        return file_name,folder_path
    except BaseException as e:
        print("Exception in get_filename_and_path function")
        print("Error on line {}:".format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)


def verify_arguments(argv):
    """
    Verifies command line arguments count and directories exists or not
    Verifies source and target file paths and creates output directory if not exist
    @param argv: Arguments list
    @return: boolean true or false. True when arguments are valid otherwise False
    """
    try:
        arguments_count = len(argv)
        if arguments_count == 3:  # To verify number of command line arguments
            if argv[1] == argv[2]:  # To verify source and target file paths
                print("Input and output files are same. Please check file name(s) and Path")
                return False
            else:
                input_file_name, input_folder_path = get_filename_and_path(argv[1])
                output_file_name, output_folder_path = get_filename_and_path(argv[2])
                if input_file_name and output_file_name:  # To verify file names are not empty
                    if not os.path.exists(output_folder_path):
                        print("Creating output directory")
                        os.mkdir(output_folder_path)      # Create output directory if not exist
                    return True
                else:
                    print("Invalid File Names")
                    return False
        else:
            print("Invalid Number of Arguments")
            return False
    except BaseException as e:
        print("Exception in verify_arguments function")
        print("Error on line {}:".format(sys.exc_info()[-1].tb_lineno), type(e).__name__,e)
        return False


def update_header(input_file_header):
    '''
    To update csv file header record with python friendly Name
    @param input_file_header: File header
    @return: File header with friendly names
    '''
    fieldnames = []
    for header in input_file_header:
        new_header = python_friendly_name(header)
        fieldnames.append(new_header)
    return fieldnames


def python_friendly_name(name):
    '''
    To convert a string to python friendly Name
    @param name: A header value
    @return: header with friendly name
    '''
    nice_name = re.sub('\W+',' ',name).lower().strip().replace(' ','_')
    return nice_name


def clean_strings(value):
    '''
    To trim any trailing whitespace
    @param value: String
    @return: String
    '''
    new_value = str(value.strip())
    return new_value


def convert_to_bool(value):
    '''
    To Conver YES and NO values to boolean True and False
    @param value: String
    @return: boolean True or False
    '''
    if value.upper() in ('KNOWN','1'):
        new_value = True
    elif value.upper() in ('UNKNOWN','0'):
        new_value = False
    else:
        new_value = None
    return new_value


def box_office_to_float(box_office, k=1000):
    '''
    To convert total box office amount to float with millions format
    @param box_office:
    @param k:
    @return: float (Example: $532K as 0.532M)
    '''
    num_float = 0
    try:
        if len(box_office)>1:
            is_millions = box_office[-1]
            amount = float(box_office[1:-1])
            if is_millions == 'K':
                if amount % k == 0:
                    num_float = int(amount / k)
                else:
                    num_float = float(amount / k)
            else:
                num_float = amount
        else:
            num_float = 0
    except BaseException as e:
            print("Exception in box_office_to_float function")
            print("Error on line {}:".format(sys.exc_info()[-1].tb_lineno), type(e).__name__,e)
    return num_float


def transform_record(record):
    '''
    To transform a record
    @param record: Avenger record
    @return: Avenger record with transformed values
    '''
    try:
        for key, value in record.items():
            if key == 'number_of_subjects' or key == 'year_release':
                record[key] = int(record[key])
            if key == 'race_known' or key == 'person_of_color':
                record[key] = convert_to_bool(record[key])
            if key == 'year_release':
                currentYear = date.today().year
                year = currentYear - int(record['year_release'])
                record['years_since_released'] = year
            if key == 'box_office':
                record[key] = box_office_to_float(record['box_office'])
            record['title'] = clean_strings(record['title'])
            record['director'] = clean_strings(record['director'])
            record['subject'] = clean_strings(record['subject'])
            record['subject_race'] = clean_strings(record['subject_race'])
            record['lead_actor_actress'] = clean_strings(record['lead_actor_actress'])
        return record
    except BaseException as e:
        print("Exception in transform_record function")
        print("Error on line {}:".format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
