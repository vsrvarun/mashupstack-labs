# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
import random
import copy
letters = ['a', 'e', 'i', 'o', 'u']
length = len(letters)
# calculating no of possible strings
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
no_of_permutations = factorial(length)
result = []
# initializing length of result as 1
length_result = 1
# taking deep copy to shuffle a copy of list
letters_copy = copy.deepcopy(letters)
while length_result <= no_of_permutations:
    random.shuffle(letters_copy)
    random_string = ''.join(letters_copy)
    if random_string not in result:
        result.append(random_string)
    # updating length of result
    length_result = 1 + len(result)
print("Characters: ", letters)
print("The number of possible different strings are:", len(result))
print("The srings are \n", result)


