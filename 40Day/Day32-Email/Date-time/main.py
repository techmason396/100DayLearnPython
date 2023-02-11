import datetime as dt

# lấy mốc thời gian hiện tại
now = dt.datetime.now()
# lấy năm
year = now.year
# lấy tháng
month = now.month
# lấy ngày
day = now.day
# lấy giờ
hours = now.hour
print(day, month, year, hours)

# lấy ngày trong trong tuần
day_of_week = now.weekday()
print(day_of_week)

# setting date time
date_of_birth = dt.datetime(
    year=1993, month=11, day=30, hour=3, minute=30, second=30)
print(date_of_birth)
