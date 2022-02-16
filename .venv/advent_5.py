import re
import json
import pprint

example_input = ".venv/advent_5_example.txt"
input = ".venv/advent_5_input.txt"
with open(example_input) as file:
    data =  file.read()

# prog = re.compile(r"(\b\d+,\d+\b)+")
# result = prog.findall(data)
# result = [eval(i) for i in result]

prog = re.compile(r"(\b\d+\b)+")
result = prog.findall(data)
result = [int(i) for i in result]

grid_size = [max(result[0:len(result):2]), max(result[1:len(result):2])]
points_list = [result[i:i+2] for i in range(0,len(result),2)]
lines_list = [points_list[i:i+2] for i in range(0, len(points_list),2)]
print(grid_size)
pprint.pprint(lines_list)
