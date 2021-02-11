import datetime

date_str = 'Thu Feb 11 17:01:34 2021'
format_str = '%a %b %d %H:%M:%S %Y'
dt = datetime.datetime.strptime(date_str, format_str)
print(dt)
print(dt.tzinfo)


date_str_tz = 'Thu Feb 11 17:07:53 JST 2021'
format_str_tz = '%a %b %d %H:%M:%S %Z %Y'
dt_tz = datetime.datetime.strptime(date_str_tz, format_str_tz)
print(dt_tz)
print(dt_tz.tzinfo)  # None

date_str_tz = 'Thu Feb 11 17:21:52 +0900 2021'
format_str_tz = '%a %b %d %H:%M:%S %z %Y'
dt_tz = datetime.datetime.strptime(date_str_tz, format_str_tz)
print(dt_tz)
print(dt_tz.tzinfo)  # None
