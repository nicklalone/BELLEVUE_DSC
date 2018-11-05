import datetime
import calendar

def get_month(input):
   abr_num_mon_key_value = {val: key for key,val in enumerate(calendar.month_abbr)}
   a = input.split('-')
   if len(a[0]) == 3:
        return abr_num_mon_key_value[a[0]]
   else:
        return abr_num_mon_key_value[a[1]]

def get_date_joined(year,intro):
    month = get_month(intro)
    return datetime.date(int(year),month,1)

def days_since_joined(year,intro):
    date_of_joining = get_date_joined(year,intro)
    todays_date = datetime.datetime.now().date()
    return abs((todays_date - date_of_joining).days)


