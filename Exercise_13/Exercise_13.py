'''
Exercise 13

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the
sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def main():
    user_input = get_non_negative_integer()
    result = get_fibonnaci(user_input)
    print('Here are the first {} Fibonnaci numbers: {}'.format(user_input, result))
    return
              
def get_non_negative_integer(help_text = 'Please Enter an non-negative integer: '):
    while True:
        try:
            input_non_negative_integer = int(input(help_text))
        except ValueError:
            print('Ivalid input. ', end = '')
            continue
        if input_non_negative_integer < 0:
            print('Ivalid input. ', end = '')
            continue
        break
    return input_non_negative_integer

def get_fibonnaci(x):
    result = [1, 1]
    if x == 0:
        return []
    elif x == 1:
        return [1]
    elif x == 2:
        return [1, 1]
    
    while len(result) < x:
        result.append(result[-1]+result[-2])
        
    return result

if __name__ == "__main__":
    main()
    

