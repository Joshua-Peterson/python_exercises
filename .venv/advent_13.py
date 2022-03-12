import pprint
import numpy as np
import matplotlib.pyplot as plt


example_input = ".venv/advent_13_example.txt"
input = ".venv/advent_13_input.txt"

with open(input) as file:
    dots =  file.read().splitlines()
    dots = [i.split(',') for i in dots]
    dots = [[int(i) for i in j] for j in dots]

grid_x = max([i[0] for i in dots])
grid_y = max([i[1] for i in dots])



example_instructions = [['y',7], ['x',5]]

instructions = [['x',655],['y',447],['x',327], ['y',223], ['x',163], ['y',111], ['x',81], ['y',55], ['x',40], ['y',27], ['y', 13], ['y',6]]

string_instructions = """fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6"""



def fold_up(horiz, dots):
    for i in dots:
        if i[1] > horiz:
            i[1] = 2*horiz-i[1]

def fold_left(vert, dots):
    for i in dots:
        if i[0] > vert:
            i[0] = 2*vert-i[0]

def main():
    for i in instructions:
        if i[0] == 'y':
            fold_up(i[1],dots)
        else:
            fold_left(i[1],dots)
    unique_dots = []
    for i in dots:
        if i not in unique_dots:
            unique_dots.append(i)
    print(len(unique_dots))
    x = [i[0] for i in unique_dots]
    y = [-i[1] for i in unique_dots]
    # data = np.array(dots)
    # x, y = data.T
    plt.scatter(x, y)
    plt.xlim([-20, 50])
    plt.ylim([-10,10])
    plt.show()

if __name__ == "__main__":
    main()