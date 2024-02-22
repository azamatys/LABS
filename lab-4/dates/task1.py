import datetime

a = datetime.datetime.now()

b = a - datetime.timedelta(days=5)

print(b.strftime("%c"))