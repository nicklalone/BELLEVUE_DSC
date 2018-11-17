"""
utils.py - module of datetime utilities
"""
import datetime as dt

def get_month(date_string):
    """
    Takes in an input string from the intro field and returns the integer month
    """
    try:
        date = dt.datetime.strptime(date_string, '%b-%y')
    except:
        date = dt.datetime.strptime(date_string, '%d-%b')

    int_month = date.month
    return int_month


def get_date_joined(year, date):
    import datetime
    int_month = get_month(date)
    return datetime.date(int(year), int_month, 1)


def days_since_joined(year, date):
    import datetime
    today = datetime.date.today()
    since_joined = today - get_date_joined(year, date)
    return since_joined
