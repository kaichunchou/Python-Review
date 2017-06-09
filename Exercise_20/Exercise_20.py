'''
Exercise 20

Write a function that takes an ordered list of numbers (a list where the elements are in order
from smallest to largest) and another number. The function decides whether or not the given
number is inside the list and returns (then prints) an appropriate boolean.

Extras:

- Use binary search.
'''

from random import randint

def main():
    ordered_list = generate_ordered_list()
    print(ordered_list)
    user_input = get_int()
    
    if binary_search(ordered_list, user_input):
        print('{} is in the list'.format(user_input))
    else:
        print('{} is not in the list'.format(user_input))
    return
              
def generate_ordered_list():
    list_ = [randint(0,1000) for r in range(randint(30,50))]
    list_.sort()
    return list_

def binary_search(list_, num):
    result = False
    first, last = 0, len(list_)-1
    while last >= first:
        middle = int((first+last)/2)
        if list_[middle] < num:
            first = middle + 1
        elif list_[middle] > num:
            last = middle - 1
        else:
            return True       
    return False

def get_int():
    while True: #handle input
        try:
            input_int = int(input('Please enter an integer: '))
        except ValueError:
            print('Invalid input. ', end = '')
            continue
        break
    return input_int

if __name__ == "__main__":
    main()
    

