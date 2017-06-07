'''
Exercise 9

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
from random import randint

def main():
    to_guess = randint(1,9)
    num_try = 0
    while True:   
        while True: #handle input
            try:
                guess = input('Please guess the secret number(enter quit to exit): ')
                guess = guess.lower()
                if guess == 'quit':
                    return
                guess = int(guess)
            except ValueError:
                print('Invalid input. ', end = '')
                continue
            num_try += 1
            break
        
        if guess == to_guess:
            print('You have guessed {} times to find the secret number {}'.format(num_try, to_guess))
            to_guess = randint(1,9)
            num_try = 0
        elif guess > to_guess:
            print('Too high!')
        else:
            print('Too low!')
  
if __name__ == "__main__":
    main()
    

