'''
Exercise 11

Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
'''

def main():
    user_input = get_positive_integer()
    divisors = get_divisor(user_input)
    if user_input == 1:
        print('{} is not a prime number, it is an unit!'.format(user_input))
    elif len(divisors) < 3:
        print('{} is a prime number'.format(user_input))
    else:
        print('{} is not a prime number, it has the following divisors: {}'.format(user_input, divisors))
    return
              
def get_positive_integer(help_text = 'Please Enter an positive integer: '):
    while True:
        try:
            input_positive_integer = int(input(help_text))
        except ValueError:
            print('Ivalid input. ', end = '')
            continue
        if input_positive_integer < 1:
            print('Ivalid input. ', end = '')
            continue
        break
    return input_positive_integer

def get_divisor(x):
    result = []
    for num in range(1, x + 1):
        if x % num == 0:
            result.append(num)
    return result

if __name__ == "__main__":
    main()
    

