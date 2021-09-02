# Write a program that asks the user to enter their name and their age. 
# Print out a message that greets them and that tells them the year that they will turn 100 years old.
from datetime import date
name = str(input("Enter your name "))
age = int(input("Enter your age "))
current_year = date.today().year
hundredth_year = (current_year - age) + 100
print("Hello", name)
print("You will turn 100 years old on", hundredth_year)
