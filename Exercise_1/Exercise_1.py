'''
Exercise 1

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

from datetime import datetime

def main():
    while True: #handle inputs
        try:
            name, dob_yyyy, dob_mm, dob_dd, target_age, copy = input('Please enter NAME YYYY MM DD TARGETAGE NUM_COPY\n').split()
        except ValueError:
            print('Please enter valid inputs')
            continue
        try:#check input format
            birthday = datetime(int(dob_yyyy),int(dob_mm),int(dob_dd))
        except ValueError:
            correctDate = False
            print('Please enter a valid date')
            continue
        try: #handle Feburary 29
            target_date = datetime(int(dob_yyyy) + int(target_age), int(dob_mm), int(dob_dd))
        except ValueError:
            target_date = datetime(int(dob_yyyy) + int(target_age), int(dob_mm) + 1, 1)
        break
    
    if target_date < datetime.now():
        print('You are already ' + str(target_age) + " years old")
    else:
        if target_date.year == datetime.now().year:
            result = 'You will turn ' + str(target_age) + ' this year.'
        else: 
            result = 'You will turn ' + str(target_age) + ' in ' + str(int(target_date.year) - int(datetime.now().year)) +  ' year.'
        print((result + '\n') * (int(copy)-1), end = '')
        print(result, end ='')    
    
    
if __name__ == "__main__":
    main()
    

