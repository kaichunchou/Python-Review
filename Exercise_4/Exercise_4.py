'''
Exercise 4

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

def main():
    
    while True: #handle input
        try:
            input_num = int(input('Please enter an positive integer, I will print out a list all the divisors of the number: '))
        except ValueError:
            print('Invalid input. ', end = '')
            continue
        if input_num < 1:
            print('Invalid input. ', end = '')
            continue
        break

    result = []
    for num in range(1, input_num + 1):
        if input_num % num == 0:
            result.append(num)
            
    print('{} has following dividors: {}'.format(input_num, result))
    
    
if __name__ == "__main__":
    main()
    

