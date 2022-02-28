import pprint
from statistics import median
example_input = ".venv/advent_10_example.txt"
input = ".venv/advent_10_input.txt"
with open(input) as file:
    chunks =  file.read().splitlines()

characters = {
    "(": ")", 
    "[": "]",
    "{": "}",
    "<": ">"
}
character_points = {
    ")": 3, 
    "]": 57,
    "}": 1197,
    ">": 25137
}

incomplete_character_points = {
    ")": 1, 
    "]": 2,
    "}": 3,
    ">": 4
}

opening_characters = ["(","[","{","<"]

def scan_chunk(chunk, characters=characters):
    stack = []
    for i in chunk:
        if i in characters:
            stack.append(characters[i])
        if i in characters.values():
            if i == stack[-1]:
                stack.pop()
            else:
                # return (stack[-1], i)
                return i
    return "Incomplete"
            
def complete_line(chunk, characters=characters):
    completing_characters = []
    for i in chunk:
        if i in characters:
            completing_characters.append(characters[i])
        if i in characters.values():
            if i == completing_characters[-1]:
                completing_characters.pop()
    completing_characters.reverse()
    return completing_characters
      
# pprint.pprint(chunks)

def score_line(line, points = incomplete_character_points):
    score = 0
    for i in line:
        score *= 5
        score += incomplete_character_points[i]
    return score



def main():
    # result = [scan_chunk(i,characters) for i in chunks]
    # character_counts = {
    #     ")": result.count(')'), 
    #     "]": result.count(']'),
    #     "}": result.count('}'),
    #     ">": result.count('>')
    # }
    # multiplied_counts = [character_counts[i]*character_points[i] for i in character_counts]
    # print(sum(multiplied_counts))
    #Part 2
    incomplete_lines = [i for i in chunks if scan_chunk(i,characters) == "Incomplete"]
    completions = [complete_line(chunk) for chunk in incomplete_lines]
    scores = [score_line(i) for i in completions]
    print(median(scores))
   



if __name__ == "__main__":
    main()
