import datetime

date_str = 'Thu Feb 11 17:01:34 2021'
format_str = '%a %b %d %H:%M:%S %Y'
datetime = datetime.datetime.strptime(date_str, format_str)
print(datetime)
