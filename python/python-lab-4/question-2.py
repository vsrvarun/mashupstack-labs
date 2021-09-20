# Write a Python program to subtract five days from current date
from datetime import datetime, timedelta
current = datetime.today()
difference = current - timedelta(days = 5)
print("Date before five days:", difference.date())