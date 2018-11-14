# For homework, import datetime module in Python and manipulate DC Character Data per instructions
# Utilize the datetime module to convert date joined for characters based on current date to days since joined

import datetime


def get_month(intro):
    """
    Get the month for the 'Intro' value for a given DC character
    :param intro:
    :return:
    """
    values = intro.split(',')
    # Create Dict to store the months as keys
    months = dict(
        January=1, February=2, March=3,
        April=4, May=5, June=6,
        July=7, August=8, September=9,
        October=10, November=11, December=12
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
