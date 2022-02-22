import re
import pprint

example_input = ".venv/advent_8_example.txt"
input = ".venv/advent_8_input.txt"
with open(input) as file:
    data =  file.read()
   

signal_pattern = re.compile(r"(.*)\s\|")
output_pattern = re.compile(r"\|\s(.*)")
signals = signal_pattern.findall(data)
outputs = output_pattern.findall(data)
for i in range(len(signals)):
    signals[i] = signals[i].split()
    outputs[i] = outputs[i].split()

# print(sum(1 for i in outputs if len(i) in [2, 3, 4, 7]))
def countif(li):
    return sum(1 for i in li if len(i) in [2,3,4,7])

print(sum(countif(i) for i in outputs))



# print(signals)
# print(outputs)