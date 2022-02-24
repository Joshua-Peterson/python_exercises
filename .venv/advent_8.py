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

def sort_inputs(signal): 
    for i in range(len(signal)):
        signal[i] = "".join(sorted(signal[i]))

for i in range(len(signals)):
    signals[i] = signals[i].split()
    sort_inputs(signals[i])
    outputs[i] = outputs[i].split()
    sort_inputs(outputs[i])



def countif(li):
    return sum(1 for i in li if len(i) in [2,3,4,7])

# print(sum(countif(i) for i in outputs))
print(signals)
def single_line_signal_key(signal):
    signal_key = {}
    signal_sorted = sorted(signal, key=len)
    signal_key[signal_sorted[0]] = 1
    signal_key[signal_sorted[1]] = 7
    signal_key[signal_sorted[2]] = 4
    signal_key[signal_sorted[9]] = 8
    five_len = signal_sorted[3:6]
    six_len = signal_sorted[6:9]
    four_one_diff = signal_sorted[2].replace(signal_sorted[0][0],'')
    four_one_diff = four_one_diff.replace(signal_sorted[0][1],'')
    for i in five_len:
        if all(j in i for j in signal_sorted[0]):
            signal_key[i] = 3
        elif all(j in i for j in four_one_diff):
            signal_key[i] = 5
        else:
            signal_key[i] = 2
    for i in six_len:
        if all(j in i for j in signal_sorted[2]):
            signal_key[i] = 9
        elif all(j in i for j in signal_sorted[0]):
            signal_key[i] = 0
        else:
            signal_key[i] = 6
    return signal_key

def get_output_value(output, signal_key):
    sort_inputs(output)
    output_list = [str(signal_key[i]) for i in output]
    print(output_list)
    return int("".join(output_list))








def main():
    x = [get_output_value(outputs[i], single_line_signal_key(signals[i])) for i in range(len(signals))]
    print(sum(x))
    
    

if __name__ == "__main__":
    main()