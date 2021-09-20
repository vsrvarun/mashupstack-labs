# Write a Python program to read a random line from a file.
import random
f = open('file_url', 'r')
file = f.readlines()
f.close()
line = random.randrange(0, len(file))
print("Random line of file: \n", file[line])