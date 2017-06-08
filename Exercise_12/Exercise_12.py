'''
Exercise 12

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
'''
from random import randint

def main():
    list_1 = gen_list()
    result = []
    append_first_element(list_1, result)
    append_last_element(list_1, result)
    print(list_1)
    print(result)
    return

def gen_list():
    return [randint(0,20) for r in range(randint(0,20))]

def append_first_element(list_x, result):
    if len(list_x) == 0:
        return
    else:
        result.append(list_x[0])

def append_last_element(list_x, result):
    if len(list_x) == 0:
        return
    else:
        result.append(list_x[-1])


if __name__ == "__main__":
    main()
    

