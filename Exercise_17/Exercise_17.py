'''
Exercise 17

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
'''
from random import randint

def main():
    url = 'http://www.nytimes.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    result = soup.find_all(class_ = 'story-heading')
    for heading in result:
        if heading.a: 
            print(heading.a.text.replace("\n", " ").strip())
        else: 
            print(heading.contents[0].strip())
    

if __name__ == "__main__":
    main()
    

