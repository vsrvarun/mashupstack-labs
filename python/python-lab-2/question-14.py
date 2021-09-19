# Write a Python program to remove an item from a set if it is present in the set.
sets = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A'}
print(sets)
input = input("Enter an item from the avove set ") 
try:
    item = int(input)
except: 
    item = str(input)
finally:
    sets.discard(item)
print(sets)