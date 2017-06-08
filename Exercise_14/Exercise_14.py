'''
Exercise 14

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

- Write two different functions to do this - one using a loop and constructing a list, and another using sets.
- Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

#Using hash look up table to make the complexity to O(n+m)

from random import randint

def main():

    list_1 = gen_list()
    result_1 = set_method(list_1)
    result_2 = loop_method(list_1)
                
    list_1.sort() #sort for human to check for mistake(O(nlogn)
    result_1.sort()
    result_2.sort()
    print('List 1: {}'.format(list_1))
    print('Set method: {}'.format(result_1))
    print('Loop method: {}'.format(result_2))

def gen_list():
    return [randint(0,20) for r in range(randint(0,20))]    

def loop_method(list_):
    result = []

    if list_ == []:
        return result
    
    for x in range(0, len(list_)):
        if list_[x] not in result:
            result.append(list_[x])
                   
    return result
    
def set_method(list_):
    return list(set(list_))

if __name__ == "__main__":
    main()
    

