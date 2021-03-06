'''
Exercise 10

This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

Extra:

1. Randomly generate two lists to test this
'''

#Using hash look up table to make the complexity to O(n+m)
from random import randint

def main():

    list_1 = [randint(0,20) for r in range(randint(10,20))]
    list_2 = [randint(0,20) for r in range(randint(10,20))]
    result = [a for a in set(list_1) if a in list_2]
                
    list_1.sort() #sort for human to check for mistake(O(nlogn)
    list_2.sort()
    result.sort()
    
    print('List 1: {}'.format(list_1))
    print('List 2: {}'.format(list_2))
    print('Result: {}'.format(result))
    
    
if __name__ == "__main__":
    main()
    

