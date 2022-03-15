import pprint

example_input = ".venv/advent_14_example.txt"
input = ".venv/advent_14_input.txt"

with open(input) as file:
    rules_list =  file.read().splitlines()
    rules_list = [i.split(' -> ') for i in rules_list]
    rules = {i[0]:i[1] for i in rules_list}

pprint.pprint(rules)
example_polymer = "NNCB"
polymer = "FSKBVOSKPCPPHVOPVFPC"

def build_polymer(polymer=polymer, rules=rules, steps=10):
    new_polymer = ''
    last = polymer[-1]
    for i in range(len(polymer)-1):
        new_polymer += polymer[i]
        pair = polymer[i] + polymer[i+1]
        if pair in rules:
            new_polymer += rules[pair]
    new_polymer += last
    steps -= 1
    # print(new_polymer)
    if steps > 0:
       return build_polymer(new_polymer,rules,steps)
    return new_polymer


def main():
    final_poly = build_polymer()
    print(len(final_poly))
    char_counts = {i : final_poly.count(i) for i in set(final_poly)}
    print(char_counts)
    part_1 = max(char_counts.values()) - min(char_counts.values())
    print(part_1)


if __name__ == "__main__":
    main()