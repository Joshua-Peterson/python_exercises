"""Web Scraping Project
Introduction
In this project you'll be building a quotes guessing game. When run, your program will scrape a website for a collection of quotes. Pick one at random and display it. The player will have four chances to guess who said the quote. After every wrong guess they'll get a hint about the author's identity.

Requirements
Create a file called `scraping_project.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com
You can use `bs4` and `requests` to get the data. For each quote you should grab the text of the quote, the name of the person who said the quote, and the href of the link to the person's bio. Store all of this information in a list.
Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!
After every incorrect guess, the player receives a hint about the author. 
For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the player the author's birth date and location.
The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.
When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.
Good luck!"""

import requests
from random import choice
from bs4 import BeautifulSoup

def first_clue(page_url):
    page = requests.get('http://quotes.toscrape.com'+ page_url)
    soup = BeautifulSoup(page.text, "html.parser")
    return (soup.find(class_= "author-born-date").get_text() + " " + soup.find(class_ = "author-born-location").get_text())
# def get_pages(soup):
    
#     pages = [soup]
#     next_url = soup.find(class_"next", href=True)
#     next_page = requests.get('http://quotes.toscrape.com/')

def get_info(soup):
    quotes = soup.find_all(class_="quote")
    info = []
    for i in quotes:
        info.append([i.find(class_="text").get_text(),i.find(class_= "author").get_text(),i.find(href=True)['href']])
    return info

page = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(page.text, "html.parser")
info = get_info(soup)
next_button = soup.find(class_="next")
while next_button:
    new_page = requests.get(f"http://quotes.toscrape.com{next_button.find(href=True)['href']}")
    new_soup = BeautifulSoup(new_page.text, "html.parser")
    info += get_info(new_soup)
    next_button = new_soup.find(class_="next")

print(info)
# info = {}
# for i in quotes:
#     info[i.find(class_= "author").get_text()] = [i.find(class_="text").get_text(), i.find(href=True)['href']]
# print(info)

#Game Logic
while True:
    guesses_remaining = 4
    quote_info = choice(info)
    print(f"Who said this?\n{quote_info[0]}")
    
    while guesses_remaining > 0:
        guess = input("Answer: ")
        name = quote_info[1]
        split_name = name.split()
        if guess == name:
            print ("That is correct!")
            break 
        else:
            guesses_remaining -= 1
            if guesses_remaining == 3:
                print(f"Sorry! You suck...Here's a hint\nThis person was born {first_clue(quote_info[2])}")
            elif guesses_remaining == 2:
                print(f"Sorry! You suck...Here's a hint\nThe first letter of their first name is {split_name[0][0]}")
            elif guesses_remaining == 1:
                print(f"Sorry! You suck...Here's a hint\nThe first letter of their last name is {split_name[1][0]}")
            else: 
                print(f"You lose, good day sir!....P.S. the answer was {name}")
    if input("Play again? y/n ") != "y":
        break
