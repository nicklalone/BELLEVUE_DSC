from datetime import datetime

def get_month(year, intro):
    month = get_date_joined(year, intro).month
    return month
def get_date_joined(year, intro):
    if intro[0] in ('1','2','3','4','5','6','7','8','9'):
        temp_date = '1 ' + intro[-3:] + ' ' + year[2:]
    else:
        temp_date = '1' + ' ' + intro.replace('-', ' ')
    join_date = datetime.strptime(temp_date, "%d %b %y").date()
    return join_date

def days_since_joined(year,intro):
    date_joined = get_date_joined(year,intro)
    elapsed_days = datetime.today().date() - date_joined
    return elapsed_days.days
