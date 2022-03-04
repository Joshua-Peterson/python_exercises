import pprint
from dataclasses import dataclass
from typing import ClassVar

example_input = ".venv/advent_11_example.txt"
input = ".venv/advent_11_input.txt"
# with open(example_input) as file:
#     energy =  file.read().splitlines()
#     for index, item in enumerate(energy):
#              energy[index] = [int(j) for j in item]
@dataclass
class Octopus:
    energy: int
    flashed: bool
    flash_counter: int
    octoflash: ClassVar[int] = 0


    def increment(self):
        if not(self.flashed): 
            self.energy += 1 
    
    def flash(self):
        self.energy = 0
        self.flashed = True
        Octopus.octoflash += 1

with open(input) as file:
    energy =  file.read().splitlines()
    for index, item in enumerate(energy):
         energy[index] = [Octopus(int(j), False, 0) for j in item]

energy_padded = energy
for i in energy_padded:
    i.insert(0,Octopus(0,True,0))
    i.append(Octopus(0,True,0))

energy_padded.insert(0, [Octopus(0,True,0) for j in energy_padded[0]])
energy_padded.append([Octopus(0, True,0) for j in energy_padded[0]])


# def step_one(matrix):
#     for row in matrix:
#         for index, item in enumerate(row):
#             row[index] = 1 + item

def step_one(matrix):
    for row in matrix[1:len(matrix)-1]:
        for item in row[1:len(row)-1]:
            item.increment()
            

def raise_adjacent(matrix):
    for row_num, row in enumerate(matrix[1:len(matrix)-1]):
        for col, octopus in enumerate(row[1:len(row)-1]):
            if octopus.energy > 9:
                octopus.flash()
                octopus.flash_counter += 1
                matrix[row_num+1][col+2].increment()
                matrix[row_num+1][col].increment()
                matrix[row_num+2][col+1].increment()
                matrix[row_num][col+1].increment()
                matrix[row_num+2][col+2].increment()
                matrix[row_num+2][col].increment()
                matrix[row_num][col+2].increment()
                matrix[row_num][col].increment()
                # pprint.pprint(matrix)
                raise_adjacent(matrix)

def step_three(matrix):
    for row in matrix[1:len(matrix)-1]:
        for item in row[1:len(row)-1]:
            item.flashed = False

def count_flashes(matrix):
    flashes = 0
    for row in matrix[1:len(matrix)-1]:
        for octopus in row[1:len(row)-1]:
            flashes += octopus.flash_counter
    return flashes

def all_flashed(matrix):
    for row in matrix[1:len(matrix)-1]:
        for octopus in row[1:len(row)-1]:
            if octopus.flashed == False:
                return False
    return True
                  


def main():
    # PART 1
    for i in range(100):
        step_one(energy_padded)
        raise_adjacent(energy_padded)
        step_three(energy_padded)
    # pprint.pprint(energy_padded)
    print(Octopus.octoflash)
    # pprint.pprint(count_flashes(energy_padded))

# PART 2
    # safe_step = 0
    # while True:
    #     step_one(energy_padded)
    #     raise_adjacent(energy_padded)
    #     safe_step += 1
    #     if all_flashed(energy_padded):
    #         break
    #     step_three(energy_padded)
    # print(safe_step)
 

    

if __name__ == "__main__":
    main()
