# I have a folder with 20 files in it of different file names. Eg: sample.txt, test.txt, output.txt, addf.txt, adf.txt etc.. and so on.. 
# The files can have any content. So you can create any files you like.
# # Write a python program to get all the filenames of the files and print them in an ascending order.
import os
# Provide directory url. you can revmove the line if you are run in same directory.
os.chdir("directory_url")
files = os.listdir()
ascend = sorted(files, key=str.lower)
print("Files in ascending order:")
for file in ascend:
    print(file)