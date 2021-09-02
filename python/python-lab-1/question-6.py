# Ask the user for a string and print out whether this string is a palindrome or not
input_word = str(input("Enter a string "))
if input_word == input_word[::-1]:
    print("The string is palindrome")
else:
    print("The string is not a palindrome")