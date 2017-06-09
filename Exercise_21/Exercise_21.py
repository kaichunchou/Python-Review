'''
Exercise 21

Take the code from the How To Decode A Website exercise (if you didn’t do it or
just want to play with some different code, use the code from the solution), and
instead of printing the results to a screen, write the results to a txt file. In
your code, just make up a name for the file you are saving to.

Extras:

- Ask the user to specify the name of the output file that will be saved.
'''
from random import randint
import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://www.nytimes.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    result = soup.find_all(class_ = 'story-heading')
    with open('file_to_save.txt', 'w') as open_file:        
        for heading in result:
            if heading.a: 
                open_file.write(heading.a.text.replace("\n", " ").strip() + "\n")
            else: 
                open_file.write(heading.contents[0].strip() + "\n")
    

if __name__ == "__main__":
    main()
    

