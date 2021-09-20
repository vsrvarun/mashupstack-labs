# Write a Python program to read a file line by line store it into a variable
f = open('file_url', 'r')
variable = f.readlines()
f.close()
print("The value of variable is \n", variable)

