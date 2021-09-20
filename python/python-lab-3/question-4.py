# Write a Python program to read last n lines of a file.
f = open('file_url', 'r')
n = int(input("Enter the number of last lines required to open \n"))
lines = []
i = 0
for x in f:
    lines.append(x)
    i += 1
f.close()
if i < n:
    print("The given file doesn't have", n, "lines")
else:
    last_index = i - n
    index = i - 1
    print("The last", n, "lines are:")
    while index >= last_index:
        print(lines[index])
        index -= 1