'''
Exercise 8

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
from getpass import getpass #use this so player 2 cannot see what player 1 is playing
def main():
    valid_input = ['rock', 'paper', 'scissors', 'quit']
    p1_score = p2_score = 0
    while True:
        
        #player 1 input
        p1_input = getpass('Player 1: Enter Rock, Paper, or Scissors to play, or quit to exit: ')
        while True:
            p1_input = p1_input.lower() 
            if p1_input in valid_input:
                if p1_input == 'quit':
                    print('Thank you for playing')
                    return
                break
            p1_input = getpass('Invalid Input. Please re-enter: ')
            
        #player 2 input
        p2_input = getpass('Player 2: Enter Rock, Paper, or Scissors to play, or quit to exit: ')
        while True:
            p2_input = p2_input.lower() 
            if p1_input in valid_input:
                if p2_input == 'quit':
                    print('Thank you for playing')
                    return
                break
            p2_input = getpass('Invalid Input. Please re-enter: ')

        #Check result
        result = ''
        if p1_input == p2_input:
            result = 'Result: draw'
        elif p1_input == 'rock':
            if p2_input == 'scissors': result = 'Result: Player 1 wins'
            elif p2_input == 'paper': result = 'Result: Player 2 wins'
        elif p1_input == 'paper':
            if p2_input == 'rock': result = 'Result: Player 1 wins'
            elif p2_input == 'scissors': result = 'Result: Player 2 win'
        else: #last condition is p1_input == scissors
            if p2_input == 'paper': result = 'Result: Player 1 wins'
            elif p2_input == 'rock': result = 'Result: Player 2 wins'
            
        if result == 'Result: Player 1 wins':
            p1_score += 1
        elif result == 'Result: Player 2 wins':
            p2_score += 1
            
        print('Player 1: {}, Player 2: {}, {}'.format(p1_input, p2_input, result))
        print('Current score: {}:{}.'.format(p1_score, p2_score))
    
if __name__ == "__main__":
    main()
    

