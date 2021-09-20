# Write a Python program to convert unix timestamp string to readable date
from datetime import datetime
timestamp = int('1632127690')
current = datetime.fromtimestamp(timestamp)
print("Date from unix timestamp:", current.date())