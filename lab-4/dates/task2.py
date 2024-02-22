import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("yesterday:", yesterday.strftime("%A"), "\ntoday:", today.strftime("%A"), "\ntomorrow:", tomorrow.strftime("%A"))