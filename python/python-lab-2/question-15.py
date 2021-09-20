# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
import random
import string
import math
from typing import final
length = int(input("Enter length of password "))
if length < 4:
    print("minimum length 4 is required")
else:
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    num = list(string.digits)
    chara = list(string.punctuation)
    # Setting number of uppercase, lowercase, characters, digit present in password
    distribution = math.floor(length/4)
    ad_distribution = length - (3 * distribution)
    def random_generator(list, no):
        random_list = random.choices(list, k = no)
        return random_list
    upper_random_list = random_generator(upper, ad_distribution)
    lower_random_list = random_generator(lower, distribution)
    num_random_list = random_generator(num, distribution)
    chara_random_list = random_generator(chara, distribution)
    final_list = upper_random_list + lower_random_list + num_random_list + chara_random_list
    random.shuffle(final_list)
    password = ''.join(final_list)
    print("Your strong password is \n", password)




