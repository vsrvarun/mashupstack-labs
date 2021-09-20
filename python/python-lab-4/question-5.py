# Write a Python program to get days between two dates. Go to the editor 
# Exampe: days between 28/02/2000 and  28/02/2001
from datetime import date
new_date = date(2001, 2, 28)
old_date = date(2000, 2, 28)
difference = new_date - old_date
print("Days between", old_date, "and", new_date, ":", difference.days)