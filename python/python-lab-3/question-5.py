# Write a Python program to read a file line by line and store it into a list.
f = open('file_url', 'r')
file_list = []
for x in f:
    file_list.append(x)
f.close()
print("Here is the list \n", file_list)
