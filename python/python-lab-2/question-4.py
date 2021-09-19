# Write a python program to count repeated characters in a string.
string = input("Enter a string ")
freaquency = {}
for x in string:
    if x in freaquency:
        freaquency[x] += 1
    else:
        freaquency[x] = 1
count = 0
repeated = {}
for x in freaquency:
    if freaquency[x] > 1:
        count += freaquency[x]
        repeated[x] = freaquency[x]
print("Total number of repeated characters:", count)
print("Reapeated characters are:", repeated)
