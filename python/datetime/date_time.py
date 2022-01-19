# how to get current date and time

import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)
print()


# ==================================================
# date
# ==================================================

# how to get current date
date_object = datetime.date.today()
print(date_object)
print()

# how to create a dateobject
d = datetime.date(2019, 4, 13)
print(d)
print()

from datetime import date

# how to get a date from the timestamp
timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)
print()

# how to print today's year, month and day
# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
print()


# ==================================================
# time
# ==================================================

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
print()

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)
print()

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)
print()

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)
print()

# how to print hour, minute, second and microsecond
a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)
print()

# how to print year, month, hour, minute and timestamp
from datetime import datetime

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())
print()

# how to find difference between two dates and times
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))  
print()

# how to find difference between two timedelta objects
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print()

# how to find time duration in seconds
t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())
print()

# how to print current date in different formats
today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
print()