import datetime
import re
from msds510.utils import date


def get_value(series, value):
    """takes an incoming list and an item. if item exists in series,
        return index of where the item exists.  If the items are a
        dictionary, it should return the value associated with the
        input key. The function should return None if no value is found.
    Args:
        series: a list, tuple or dictionary of items
        value: an integer index or  value, depending on if is list or dict
    Returns:
        an integer or None - when can't be converted
    """
    try:
        return series.index(value)
    except Exception:
        try:
            return series[value]
        except Exception:
            return None


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


def to_bool(value):
    """takes an incoming string (empty, YES, NO)
        and converts it to a boolean value
    Args:
        value: a string
    Returns:
        a bool or None.
    """
    if not value.strip():
        return None
    else:
        return True if value == 'YES' else False


def clean_notes(value):
    """takes an incoming string and strips
        empty string and newlines from the ends.
    Args:
        value: a string
    Returns:
        a string less empty values on the ends.
    """
    return value.strip()


def make_nice_name(name):
    """Formats string for use as dictionary key
    Args:
        name: an unformatted string

    Returns:
        a formatted string with spaces and slashes
        replaced with underscores, empty characters
        stripped, non-alpha-num removed and all
        converted to lower case.
    """
    newString = name.replace(" ", "_")
    newString = newString.replace("/", "_")
    newString = newString.strip("?").strip().lower()
    newString = re.sub(r'[^0-9a-z_\_]', '', newString)
    return newString


def clean_field_names(data):
    """takes a list of dictionary records,
        makes the keys for each dictionary record
        python friendly, and returns a list of the
        newly formatted data.
    Args:
        data: a list of dictionary records

    Returns:
        a newly formatted list of dictionary records
    """
    retdata = []
    for d in data:
        newRow = {}
        for key, val in d.items():
            newRow[make_nice_name(key)] = d[key]
        newRow = transform_record(newRow)
        retdata.append(newRow)
    return retdata


def transform_record(rdict):
    """takes a dictionary record and converts the
        values for to their expected format
    Args:
        rdict: a single dictionary records

    Returns:
        a dictionary with newly formatted values
    """
    rdict['year'] = to_int(rdict['year'])


    return rdict
