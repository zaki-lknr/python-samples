import datetime

# datetime.now(): 現在のローカルな日時を返します。
date_now = datetime.datetime.now()
print(date_now)
print(date_now.tzinfo)  # None

date_utc = datetime.datetime.now(tz=datetime.timezone.utc)
print(date_utc)
print(date_utc.tzinfo)  # UTC

# date_jst = datetime.datetime.now(tz=datetime.timezone.jst)
#### AttributeError: type object 'datetime.timezone' has no attribute 'jst'
# print(date_jst)
# print(date_jst.tzinfo)

# Python3のdatetimeはタイムゾーンを指定するだけで高速になる - Qiita
# https://qiita.com/mattsu6/items/5511c5631e7a54550f7f
tz_jst = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
date_jst = datetime.datetime.now(tz=tz_jst)
print(date_jst)
print(date_jst.tzinfo)  # JST

tz_c = datetime.timezone(datetime.timedelta(hours=+9), 'curry')
date_c = datetime.datetime.now(tz=tz_c)
print(date_c)
print(date_c.tzinfo)  # curry

tz_j = datetime.timezone(datetime.timedelta(hours=+9))
date_j = datetime.datetime.now(tz=tz_j)
print(date_j)
print(date_j.tzinfo)  # UTC+09:00


