import datetime

date_now = datetime.datetime.now()
print(date_now)
print(date_now.tzinfo)  # None

str = date_now.strftime("%Y-%m-%d (%Z) %H-%M-%S.%f")
print(str)

tz_jst = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
date_jst = datetime.datetime.now(tz=tz_jst)
print(date_jst)
print(date_jst.tzinfo)  # JST

str = date_jst.strftime("%Y-%m-%d %a %b (%Z) %H-%M-%S.%f")
print(str)
