# Write a Python program to get week number from 16/06/2015
from datetime import date
import math
current = date.today()
old = date(2015, 6, 16)
date_diff = current - old
week_no = math.floor((date_diff.days) / 7)
current_week_no = current.strftime("%U")
print("Week number from 16/06/2015:", week_no)