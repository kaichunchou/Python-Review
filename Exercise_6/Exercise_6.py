'''
Exercise 6

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

def main():
    
    while True: #handle input
        try:
            input_str = input('Please enter a string to check if it is a palindrome or not:\n')
        except ValueError:
            print('Invalid input. ', end = '')
            continue
        break

    is_palindrome = 'is'
    i = 0
    j = len(input_str)-1
    while j > i:
        if input_str[j] != input_str[i]:
            is_palindrome = 'is not'
            break
        i += 1
        j -= 1

    print('{} {} a palindrome'.format(input_str, is_palindrome))

    
if __name__ == "__main__":
    main()
    

