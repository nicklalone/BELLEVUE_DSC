import datetime
'''
This is a utility module that holds some functions that are used
to find the date the character joined as well as calculate the 
number of days elapsed since the character joined.
'''

'''This section of code splits the intro field into two parts.
The dictionary is used to assign months to numbers.
Each part is then checked against the dictionary
to determine the month value.
'''

def get_month(intro):

    values = intro.split('-')
    months = dict(
        Jan=1, Feb=2, Mar=3, Apr=4, May=5, Jun=6,
        Jul=7, Aug=8, Sep=9, Oct=10, Nov=11, Dec=12
    )

    if values[0] in months:
        return months[values[0]]
    elif values[1] in months:
        return months[values[1]]


def get_date_joined(year_str, intro):
    '''
    This section relies on the get_month function above.
    It takes a year and an intro argument and returns
    a datetime object of when the character joined.
    Since some start dates are only months, all start
    dates are set to the first of the month.
    '''
    month = get_month(intro)
    year = int(year_str)

    return datetime.date(year, month, 1)


def days_since_joined(year, intro):
    '''
    This function takes the year and intro fields
    and returns the number of days from today's
    date that have elapsed.
    '''
    today = datetime.date.today()
    date_joined = get_date_joined(year, intro)
    return (today-date_joined).days
