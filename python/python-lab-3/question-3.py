# Write a Python program to append text to a file and display the text.
f = open('file_url', 'a')
txt = input("Enter text to append file \n")
f.write("\n")
f.write(txt)
f.close()
f = open('file_url', 'r')
print(f.read())
f.close()