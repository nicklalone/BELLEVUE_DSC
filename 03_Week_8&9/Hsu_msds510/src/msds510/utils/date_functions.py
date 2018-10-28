import datetime


def get_month(input_date):
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for x in range(0, 12):
        # "if in" statement in strings checks for the substring so the input date order doesn't matter as long as it's a string.
        if months[x] in input_date.lower():
            return x + 1
    return None


def get_date_joined(input_year, input_day):
    output_month = get_month(input_day)
    output_year = int(input_year)
    return datetime.date(output_year, output_month, 1)


def days_since_joined(year, day):
    today = datetime.date.today()
    temp_date = get_date_joined(year, day)
    # Convert the date difference into days
    output_int = (today - temp_date).days
    return output_int
