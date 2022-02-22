import re
import pprint

example_input = ".venv/advent_6_example.txt"
input = ".venv/advent_6_input.txt"
with open(input) as file:
    fish =  file.read().split(",")
    fish = [int(i) for i in fish]
    

days = 256

def decrement(fish): 
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
        else:
            fish[i] -= 1
        

def initialize(fish):
    numbers = [0 for i in range(9)]
    for i in fish:
        numbers[i] = fish.count(i)
    return numbers



count = initialize(fish)
#print(count)
for day in range(days):
    new_fish = count[0]
    count[7]+= new_fish
    count.append(count.pop(0)) 
    #print(count)

print(sum(count))


def multiply(days, fish):
    for i in range(days):
        new_fish = fish.count(0)
        decrement(fish)
        fish += new_fish * [8]
        # print(fish)
    return fish

# multiply(days,fish)
# print(len(fish))
