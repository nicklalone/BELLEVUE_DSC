import datetime

def pythonize(field):
    """
    Takes a fieldname and removes space, trailing newlines, sets all characters to lowercase
    and returns pythonized names
    :return: pythonized fieldnames
    """
    new_name = field.replace(' ','_').lower().strip('\n')

def field_cleaner(field):
    """

    :param field: field to be cleaned
    :return: list of cleaned field names
    """
    new_data = []
    for f in field:
        new_header = {}
        for key, value in f.items():
            new_header[pythonize(key)] = f[key]
        new_header = transform(new_header)
        new_data.append(new_header)
    print (new_data[1]['show'])
    return new_data

def transform(dict_record):
    """
    This function takes a dictionary record and changes the date field to a datetime object
    :param dict_record: dictionary record to be modified
    :return: transformed record
    """

