# Write a python program to find the longest words.
f = open('file_url', 'r')
lines = []
for x in f:
    lines.append(x)
f.close()
strings = ""
i = 0
while i < len(lines):
    strings += lines[i]
    i += 1
longest = max(strings.split(), key=len)
print("The longest word is \n", longest)