# Write a Python program to read first n lines of a file.
n = int(input("Enter no of lines required to read "))
f = open('file_url', 'r')
i = 1
while i <= n:
    print(f.readline())
    i += 1
f.close()