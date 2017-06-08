'''
Exercise 16

Write a password generator in Python. Be creative with how you generate passwords -
strong passwords have a mix of lowercase letters, uppercase letters, numbers,
and symbols. The passwords should be random, generating a new password every time
the user asks for a new password. Include your run-time code in a main method.

Extra:

-Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

Install RandomWords here:
https://pypi.python.org/pypi/RandomWords/0.1.5
'''
from random_words import RandomWords
from random import randint
import string

def main():
    input_strength = get_strength()
    input_length = get_length()
    password = generate_password(input_strength, input_length)
    print(password)
    return

def generate_password(strength, length):
    password = ''
    while len(password) < length:
        to_fill = length - len(password)
        password += get_rnd_char(randint(1, strength), to_fill)
    
    return password

def get_rnd_char(index, max_length):
    if index == 1:
        if max_length > 2:
            return get_random_word(max_length)
        else:
            return get_random_digit()
    elif index == 2: return get_random_digit()
    elif index == 3: return get_random_lower_char()
    elif index == 4: return get_random_upper_char()
    else: return get_random_punctuation()

def get_random_word(max_length): #level 1 strength
    word = ''
    while len(word) > max_length or word == '':    
        word = RandomWords().random_word()
    return word

def get_random_digit(): #level 2 strength
    return string.digits[randint(0, len(string.digits)-1)]

def get_random_lower_char(): #level 3 strength
    return string.ascii_lowercase[randint(0, len(string.ascii_lowercase)-1)]

def get_random_upper_char(): #level 4 strength
    return string.ascii_uppercase[randint(0, len(string.ascii_uppercase)-1)]

def get_random_punctuation(): #level 5 strength
    return string.punctuation[randint(0, len(string.punctuation)-1)]


def get_strength():
    while True: #handle input
        try:
            input_str = int(input('Please enter how strong you want the password to be generated(1-5):\n'))
        except ValueError:
            print('Invalid input. ', end = '')
            continue
        if input_str > 5 or input_str < 1:
            print('Invalid input. ', end = '')
            continue
        break
    return input_str


def get_length():
    while True: #handle input
        try:
            input_len = int(input('Please enter how long you want the password to be generated(positive integer number):\n'))
        except ValueError:
            print('Invalid input. ', end = '')
            continue
        break
    return input_len

if __name__ == "__main__":
    main()
    

