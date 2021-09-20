# Write a Python program to write a list to a file.
lists = ['Hello', 'World', 'MashupStack', 'Python']
list_str = ' '.join(lists)
f = open('file_url', 'w')
f.write(list_str)
f.close()
f = open('file_url', 'r')
print(f.read())
f.close()