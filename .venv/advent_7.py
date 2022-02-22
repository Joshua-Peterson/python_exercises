import re
import pprint
from statistics import median

example_input = ".venv/advent_7_example.txt"
input = ".venv/advent_7_input.txt"
with open(input) as file:
    positions =  file.read().split(",")
    positions = [int(i) for i in positions]
    positions = sorted(positions)

# print(positions)
point = round(sum(positions)/len(positions))

def part_1_distance(li):
    med = median(li)
    distances = [abs(i-med) for i in li]
    return distances

def part_2_fuel(move):
    return sum(range(1,move+1))
    #returns cost of move

def triangular_cost(steps):
    return (steps * (steps+1)//2)

# print(sum(part_1_distance(positions)))
cost = 0
lowest_cost = sum([part_2_fuel(abs(0-i)) for i in positions])
print(lowest_cost)
for i in range(max(positions)):
    cost = sum([triangular_cost(abs(i-j)) for j in positions])
    if cost < lowest_cost:
        lowest_cost = cost

print(lowest_cost)
