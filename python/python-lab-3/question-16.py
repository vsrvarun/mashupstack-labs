# Write a Python program to remove newline characters from a file.
import random
f = open('file_url', 'r')
file = f.readlines()
f.close()
text = ''
for x in file:
    text += ''.join(x.replace('\n', ' '))
f = open('file_url', 'w')
f.write(text)
f.close()
f = open('file_url', 'r')
print("Newline characters are removed. \n", f.read())
f.close()