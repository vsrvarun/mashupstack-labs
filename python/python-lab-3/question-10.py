# Write a Python program to count the frequency of words in a file.
f = open('file_url', 'r')
content = f.readlines()
f.close()
len_content = len(content)
txt = ''
i = 0
while i < len_content:
    txt += content[i]
    i += 1
txt_list = txt.split()
frequency = {}
for x in txt_list:
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1
print(frequency)