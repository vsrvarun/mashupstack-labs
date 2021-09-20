# Write a Python program to count the number of lines in a text file.
f = open('file_url', 'r')
lines = f.readlines()
f.close()
print("Number of lines in text file:", len(lines))