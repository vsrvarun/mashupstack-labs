# Write a Python program to reverse a tuple.
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple1_list = list(tuple1)
list_reverse = tuple1_list[::-1]
tuple_reverse = tuple(list_reverse)
print("Tuple:", tuple1)
print("Reversed tuple:", tuple_reverse)