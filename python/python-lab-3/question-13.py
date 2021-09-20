# Write a Python program to copy the contents of a file to another file .
f = open('source_file_url', 'r')
content = f.readlines()
f.close()
content_str = " ".join(content)
f = open('destination_file_url', 'a')
for x in content:
    f.write(x)
f.close()
print("File sucessfully copied \n")
f = open('new_file_url', 'r')
print(f.read())
f.close()
