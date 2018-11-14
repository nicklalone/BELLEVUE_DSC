import datetime

def pythonize(field):
    """
    Takes a fieldname and removes space, trailing newlines, sets all characters to lowercase
    and returns pythonized names
    :return: pythonized fieldnames
    """
    new_name = field.replace(' ','_').lower().strip('\n')
    return new_name

def to_int(value):
    """takes an incoming numeric string and converts it
        to an int.
    Args:
        value: a numeric string
    Returns:
        an integer or None when can't be converted
    """
    try:
        return int(value)
    except Exception:
        return None

def field_cleaner(field):
    """

    :param field: field to be cleaned
    :return: list of cleaned field names
    """
    new_data = []
    for f in field:
        new_record = {}
        for key, value in f.items():
            new_record[pythonize(key)] = f[key]
        new_record = transform(new_record)
        new_data.append(new_record)
    return new_data

def transform (rdict):
    '''
    Takes a single dictionary record and transforms
     the data to the correct format
    :param rdict: single dictionary record
    :return: a dictionary with the new formatted data
    '''

    rdict['year'] = to_int(rdict['year'])
    rdict['show'] = datetransform(rdict['show'])
    rdict['years_since_aired'] = datetime.date.today().year - rdict['year']

    return rdict


def datetransform (date):
    """
    :param date: date in format mm/dd/yy
    :return: datetime object
    """
    temp_date = date.replace('/', ' ')
    date_list = temp_date.split(' ')
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])
    if year > 98:
        year = year + 1900
    else:
        year = year + 2000
    new_date = datetime.date(year, month, day)
    return new_date

if __name__ == '__main__':
    records = [
        dict(show='1/3/99'),
        dict(show='1/3/00'),
        dict(show='1/3/01'),
        dict(show='1/3/02')
    ]
    '''ex_date = '1/23/99'
    print_date = datetransform(ex_date)
    for record in records:
        record['show'] = datetransform(record['show'])
        print(record['show'])
    '''
