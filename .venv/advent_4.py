import re
import pprint
from tabnanny import check
"""2 concepts. 
1. generate numbers that would lead to win and check against next number in sequence. 
2. Check every card for a winner every draw
    Possible one row checking function and then transpose rows and columns
1 Seems more interesting but 2 seems more doable
"""

input = [10,80,6,69,22,99,63,92,30,67,28,93,0,50,65,87,38,7,91,60,57,40,84,51,27,12,44,88,64,35,39,74,61,55,31,48,81,89,62,37,94,43,29,14,95,8,78,49,90,97,66,70,25,68,75,45,42,23,9,96,56,72,59,32,85,3,71,79,18,24,33,19,15,20,82,26,21,13,4,98,83,34,86,5,2,73,17,54,1,77,52,58,76,36,16,46,41,47,11,53]
example_input = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

with open(".venv/advent_4_input.txt") as file:
    data =  file.read()

prog = re.compile(r"(\b\d{1,2}\b)+")
result = prog.findall(data)
result = [int(i) for i in result]

def make_cards(li, row_len=5, row_num=5):
    rows = [li[i:i+row_len] for i in range(0,len(li),row_len)]
    cards = [rows[j:j+row_num] for j in range(0,len(rows),row_num)]
    return cards
   
def check_card_num(card, input):
    for row in card:
        for i in range(len(row)):
            if row[i] == input:
                row[i] = "match"

def check_rows(card):
    for row in card:
        result = all(number == 'match' for number in row)
        if result:
            return result
    return False

def check_cols(card):
    transpose = [[card[j][i] for j in range(len(card))] for i in range(len(card[0]))]
    return check_rows(transpose)

def check_card(card):
    return check_rows(card) or check_cols(card)

def mark_cards(cards,input):
    for card in cards:
        check_card_num(card, input)

def bingo_w(cards, input):
    for card in cards:
        mark_cards(card, input)

def bingo_winner(cards, input):  
    for bingo_call in input:
        # for card in cards:
        #     check_card_num(card, bingo_call)
        #     if check_card(card):
        #         return [card, bingo_call]
        mark_cards(cards, bingo_call)
        for card in cards:
            if check_card(card):
                return [card, bingo_call]

def bingo_loser(cards, input):  
   for bingo_call in input:
        mark_cards(cards,bingo_call)
        for card in cards:
            if len(cards) > 1 and check_card(card):
                cards.remove(card)
            elif check_card(card):
                return [card, bingo_call]
    
def sum_unmatched(filled_card):
    tot = 0
    for row in filled_card[0]:
        tot += sum([j for j in row if isinstance(j, int)])
    return tot

def main():
    cards = make_cards(result)         
    winner = bingo_winner(cards,input)
    loser = bingo_loser(cards, input)
    print(sum_unmatched(winner)*winner[1]) 
    print(sum_unmatched(loser)*loser[1])    
    pprint.pprint(winner)
    pprint.pprint(loser)

if __name__ == "__main__":
    main()

