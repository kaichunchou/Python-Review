'''
Exercise 15

Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''

#Using hash look up table to make the complexity to O(n+m)

def main():
    user_input = get_string()
    result = reverse_words(user_input)
    print(result)
    return

def reverse_words(x):
    return ' '.join((x.split())[::-1]) 

def get_string():
    while True: #handle input
        try:
            input_str = input('Please enter a sentence to be reversed:\n')
        except ValueError:
            print('Invalid input. ', end = '')
            continue
        break
    return input_str

if __name__ == "__main__":
    main()
    

