# I have a folder with 20 files in it of different file names. Eg: 01012017.txt, 01022017.txt, 01032017.txt and so on..
# The files can have any content. So you can create any files you like.
# In this filename, 01022017.txt, the first 01 represents the date, 02 represents the month ( feb ) and 2017 represents the year.
# Write a python program to get all the filenames of the files and print them as
# Jan - 01012017.txt
# Feb - 01012017.txt
# Mar - 01032017.txt etc..
import os
from datetime import datetime
# Provide directory url. you can revmove the line if you are run in same directory.
os.chdir("directory_url")
files = os.listdir()
result = {}
# Removing file extention from files list
for x in files:
    names = ''
    for y in x:
        if y.isdigit():
            names += y
    date_obj = datetime.strptime(names, "%d%m%Y")
    month = date_obj.strftime("%b")
    result.update({x: month})
for i in result:
    print(result[i], "-", i)