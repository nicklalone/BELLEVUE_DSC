import datetime


def get_month(dateString):
    """takes a string which contains a 3 letter month
    and determines what number month of the year it is
    Args:
        dateString: a string with a 3 character month
        indicator within the string.
    Returns:
        The integer representing the month of the year
        which is represented in the input string.
    """
    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]
    for i in range(0, len(months)):
        if months[i] in dateString.lower():
            return i + 1
    return None


def get_date_joined(yearString, dateString):
    """takes a year value and a value from which
        to derive a month and uses these values
        to create a complete output date.
    Args:
        yearString: a string containing a four digit date
        dateString: a string with a 3 character month
        indicator within the string.
    Returns:
        a complete date to the first date of the month/date pair.
    """
    return datetime.date(int(yearString), get_month(dateString), 1)


def days_since_joined(yearString, dateString):
    """takes a year value and a value from which
        to derive a month and uses these values
        to calculate the days since a member joined
        the avengers.
    Args:
        yearString: a string containing a four digit date
        dateString: a string with a 3 character month
        indicator within the string.
    Returns:
        a total of days between the joining date and today's date.
    """
    dt = get_date_joined(yearString, dateString)
    rval = datetime.date.today() - dt
    rval = rval.days
    return rval
