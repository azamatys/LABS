import datetime

a = datetime.datetime(year=2015, month=12, day=9)
b = datetime.datetime(year=2006, month=7, day=7)

difference = abs(a-b)

print(difference.total_seconds())