# For homework, import datetime module in Python and manipulate Avengers Data per instructions
# Utilize the datetime module to convert date joined for characters based on current date to days since joined

import datetime


def get_month(intro):
    """
    Get the month for the 'Intro' value for a given Avenger character
    :param intro:
    :return:
    """
    values = intro.split(',')
    # Create Dict to store the months as keys
    months = dict(
        Jan=1, Feb=2, Mar=3, Apr=4, May=5, Jun=6,
        Jul=7, Aug=8, Sep=9, Oct=10, Nov=11, Dec=12
    )

    if values[0] in months:
        return months[values[0]]
    elif values[1] in months:
        return months[values[1]]


def get_date_joined(yr, intro):
    """
    Take two arguments to get the date joined for any given character based on
    year and intro record
    :param yr:
    :param intro:
    :return:
    """
    month = get_month(intro)
    year = int(yr)

    return datetime.date(year, month, 1)


def days_since_joined(year, intro):
    """
    Calculate the No. days since joined based on current date
    :param year:
    :param intro:
    :return:
    """
    today = datetime.date.today()
    date_joined = get_date_joined(year, intro)
    return (today - date_joined).days
