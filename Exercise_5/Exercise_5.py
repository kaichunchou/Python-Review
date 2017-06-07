'''
Exercise 5

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

#Using hash look up table to make the complexity to O(n+m)
from random import randint

def main():

    list_1 = [randint(0,20) for r in range(randint(10,20))]
    list_2 = [randint(0,20) for r in range(randint(10,20))]
    result = []
    D = {}
    for num in list_1:
        if num not in D:
            D[num] = ''
    for num in list_2:
        if (num in D) and (D[num] == ''):
            result.append(num)
            D[num] = ' '
            
    list_1.sort() #sort for human to check for mistake(O(nlogn)
    list_2.sort()
    result.sort()
    
    print('List 1: {}'.format(list_1))
    print('List 2: {}'.format(list_2))
    print('Result: {}'.format(result))
    
    
if __name__ == "__main__":
    main()
    

