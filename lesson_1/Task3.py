import datetime
unix_time = int(input("Enter second:"))
date = datetime.datetime.fromtimestamp(unix_time)
print(date.strftime('day:%d  time: %H:%M:%S'))