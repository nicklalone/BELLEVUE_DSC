import datetime
import re
from datetime import datetime as dt

"""
Used in process_csv.py to process the records
"""


def to_int(value):
    """
    Function takes an incoming numeric string and converts it to an int.
    Args:
        value: a numeric string
    Returns:
        an integer or None when can't be converted
    """
    try:
        return int(value)
    except :
        return None


def to_bool(value):
    """
    Function takes an incoming string (empty, YES, NO)
        and converts it to a boolean value
    Args: string value
    :return: a bool or None.
    """
    if not value.strip():
        return None
    else:
        return True if value == 'YES' else False


def get_month(mnth):
    """
    Function that takes a string which contains a 3 letter month
    and determines what number month of the year it is
    Args: a string with a 3 character month
        indicator within the string.
    :return: The integer representing the month of the year
        which is represented in the input string.
    """
    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]
    for i in range(0, len(months)):
        if months[i] in mnth.lower():
            return i + 1
    return None


def mnth_yr(st, year):
    """
    Function that takes a string and year and converts it to a standard date format
    Args: month-year string and year
    :return: date value in 2016-11-14 format
    """
    dat = str(year) + '-' + str(get_month(st)) + '-' + '01'
    return dt.strptime(dat, "%Y-%m-%d").strftime("%Y-%m-%d")


def clean_header(field):
    """
    Formats dictionary header
    Args:
        name: an unformatted string
    Returns:
        a formatted string with spaces and slashes
        replaced with underscores, empty characters
        stripped, non-alpha-num removed and all
        converted to lower case.
    """
    newheader = re.sub(r'[^0-9a-z_\_]', '', field.replace(" ", "_").replace("/", "_").strip("?").strip().lower())
    return newheader


def process_record(dict):
    """
    Function takes a dictionary record and converts the values for to their expected format
    Args:
        dict: a single dictionary records
    Returns:
        a dictionary with newly formatted values
    """

    # Adding new field to show days since first appeared in days
    dict['days_since_first_appearance'] = ''

    for key, val in dict.items():

        if key.startswith('page_id') or key.startswith('appearances') or key.startswith('year'):
            dict[key] = to_int(dict[key])

        if key == 'first_appearance':
            if len(dict[key]) != 0:
                dict[key] = mnth_yr(dict[key], dict['year'])

        if key == 'first_appearance':
            firstappearance = dict['first_appearance']
            if len(firstappearance) == 0:
                dict['days_since_first_appearance'] = ''
            else:
                fa = dt.strptime(firstappearance, "%Y-%m-%d")
                dict['days_since_first_appearance'] = (datetime.date.today() - datetime.date(fa.year, fa.month, fa.day)).days

        if key.startswith('name') or key.startswith('urlslug'):
            dict[key] = re.sub(r'[^0-9a-zA-Z_\_]', '', dict[key].replace(' ', '_').strip())

        if key.startswith('alive'):
            dict[key] = to_bool(dict[key])

    return dict


def clean(data):
    """
    This function takes a list of dictionary records, makes the keys for each dictionary record
        python friendly, and returns a list of the newly formatted data.
    Args:
        data: a list of dictionary records
    Returns:
        a newly formatted list of dictionary records
    """
    retdata = []
    for d in data:
        newRow = {}
        for key, val in d.items():
            newRow[clean_header(key)] = d[key]
        newRow = process_record(newRow)
        retdata.append(newRow)
    return retdata
