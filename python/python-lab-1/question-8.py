# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
import random
random_number = random.randrange(1, 10)
input_number = int(input("Enter a number betwwen 1 and 9 "))
if input_number == random_number:
    print("Your guess", input_number, "is exactly right")
elif input_number > random_number:
    print("Your guess", input_number, "is too high")
else:
    print("Your guess", input_number, "is too low")