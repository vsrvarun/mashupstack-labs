# Write a Python program to combine each line from first file with the corresponding line in second file.
f1 = open('file1_url', 'r')
file1 = f1.readlines()
f1.close()
f2 = open('file2_url', 'r')
file2 = f2.readlines()
f2.close()
lines_tuple = zip(file1, file2)
for x, y in lines_tuple:
    ln1 = x.replace('\n', ' ')
    ln2 = y.replace('\n', ' ')
    txt = ln1 + ln2
    print(txt)
