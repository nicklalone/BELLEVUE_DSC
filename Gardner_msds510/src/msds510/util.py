import datetime


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
    month = get_month(intro)
    year = int(year_str)

    return datetime.date(year, month, 1)


def days_since_joined(year, intro):
    today = datetime.date.today()
    date_joined = get_date_joined(year, intro)
    return (today-date_joined).days
