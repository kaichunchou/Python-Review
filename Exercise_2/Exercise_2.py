'''
Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

from datetime import datetime

def main():
    while True: #handle input
        try:
            n1 = int(input('Please enter an integer: '))
        except ValueError:
            print('Invalid input. ', end = '')
            continue
        break

    if not bool(n1 % 4):
        print('Integer ' + str(n1) + ' is multiple of 4')
    elif bool(n1 % 2):
        print('Integer ' + str(n1) + ' is odd')
    else:
        print('Ineger ' + str(n1) + ' is even')

    while True: #handle inputs
        try:
            num, check = input('Please enter one integer number and one non-zero integer divider(N1 N2): ').split()
            num = int(num)
            check = int(check)
        except ValueError:
            print('Invalid inputs.', end = '')
            continue
        if check == 0:
            print('Invalid inputs.', end ='')
        break
    
    if not bool(num % check):
        print('{} divides evenly into {}'.format(num, check), end = '')
    else:
        print('{} does not divide evenly into {}, the remainder is {}'.format(num, check, num % check), end = '')
        
        
    
if __name__ == "__main__":
    main()
    

