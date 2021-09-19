# Write a Python program to count the number of characters (character frequency) in a string.
string = input("Enter a string ")
result = {}
for x in string:
    if x in result:
        result[x] += 1
    else:
        result[x] = 1
print("Character frequency is", result)
