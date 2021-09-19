# write a program that prints out all the elements of the list that are less than 5.
# Take this list
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
output_list = []
for element in list_a:
    if element < 5:
        output_list.append(element)
print("a =", list_a)
print("The elements having a value of less than 5 are", output_list)

