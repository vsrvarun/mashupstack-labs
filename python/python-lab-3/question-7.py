# Write a Python program to read a file line by line store it into an array.
f = open('file_url', 'r')
array = []
for x in f:
    array.append(x)
f.close()
print("Here is the array \n", array)
