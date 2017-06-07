'''
Exercise 3

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

def main():
    while True: #handle input
        try:
            input_limit = int(input('a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], please enter an integer, I will print out a list smaller than that number: '))
        except ValueError:
            print('Invalid input. ', end = '')
            continue
        break

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = []
    
    for num in a:
        if num < input_limit:
            result.append(num)
    print('for loop result: {}'.format(result))
    print('one line result: {}'.format([e for e in a if e < input_limit])) 
    
if __name__ == "__main__":
    main()
    

