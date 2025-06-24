import datetime

date_now = datetime.datetime.now()
print(date_now)

custom = date_now + datetime.timedelta(days=1, hours=-1, minutes=5)
print(custom)
