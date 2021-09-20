# 1. Write a Python script to display the
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
from datetime import datetime
current = datetime.now()
print("Current date and time:", current)
print("Current year:", current.year)
print("Month of year:", current.month)
print("Week number of the year:", current.strftime("%U"))
print("Weekday of the week:", current.strftime("%A"))
print("Day of year:", current.strftime("%j"))
print("Day of the month:", current.strftime("%d"))
print("Day of week:", current.strftime("%w"), "(0 is sunday)")