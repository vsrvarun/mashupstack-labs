# Write a Python program to generate all sublists of a list.
lists = [1, 2, 3, 4]
length = len(lists)
result = []
for i in range(length):
    for j in range(1, length + 1):
        if lists[i:j] != []:
            result.append(lists[i:j])
print("Sublist of ", lists)
print(result)