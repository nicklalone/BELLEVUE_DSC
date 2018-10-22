from msds510.util import get_date_joined, days_since_joined

# Below is the given input
if __name__ == '__main__':

  records = [
    dict(year='1988', intro='Jun-88'),
    dict(year='1989', intro='May-89'),
    dict(year='2005', intro='5-May'),
    dict(year='2013', intro='13-Nov'),
    dict(year='2014', intro='14-Jan'),
    ]

# The code below iterates through the each and every dictionary in the list
# One dictionary is passed as an arguement at a time
# Empty print statement is used to create a space between the output related to each record

  for record in records:
      print("Input Record -", record)
      joinDate = get_date_joined((record['year']), (record['intro']))
      print("DateJoined =", joinDate)
      daysSince = days_since_joined((record['year']), (record['intro']))
      print("days since Joined -", daysSince, '\n')
