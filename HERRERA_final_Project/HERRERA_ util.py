import datetime

'''
to_int function
'''
def to_int(input_value):
    try:
        return int(float(input_value))
    except ValueError:
        return None

'''
get_value function
'''
def get_value(items, value):
    try:
        return items.index(value)
    except:
        try:
            return items[value]
        except:
            return None

'''
get_date_joined function
'''

def get_date_joined(year_string, month_string):
    try:
        year = int(year_string)
    except:
        return None
    month_string = month_string.lower()
    if "jan" in month_string:
        month = 1
    elif "feb" in month_string:
        month = 2
    elif "mar" in month_string:
        month = 3
    elif "apr" in month_string:
        month = 4
    elif "may" in month_string:
        month = 5
    elif "jun" in month_string:
        month = 6
    elif "jul" in month_string:
        month = 7
    elif "aug" in month_string:
        month = 8
    elif "sep" in month_string:
        month = 9
    elif "oct" in month_string:
        month = 10
    elif "nov" in month_string:
        month = 11
    elif "dec" in month_string:
        month = 12
    else:
        return None
    return datetime.date(year, month, 1)
