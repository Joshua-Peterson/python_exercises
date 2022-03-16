import pprint

example_input = ".venv/advent_14_example.txt"
input = ".venv/advent_14_input.txt"

with open(input) as file:
    rules_list =  file.read().splitlines()
    rules_list = [i.split(' -> ') for i in rules_list]
    rules = {i[0]:i[1] for i in rules_list}

rules_pairs = {i:[i[0]+rules[i], rules[i]+i[1]] for i in rules}
pair_counts = {i:0 for i in rules}
example_polymer = "NNCB"
polymer = "FSKBVOSKPCPPHVOPVFPC"
letter_counts = {i:polymer.count(i) for i in set(rules.values())}
steps = 40

for i in range(len(polymer)-1):
    pair = polymer[i] + polymer[i+1]
    pair_counts[pair] += 1

def build_polymer(polymer=example_polymer, rules=rules, steps=10):
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

def pair_counting(pair_counts=pair_counts,rules_pairs=rules_pairs, polymer=polymer, steps=steps, letter_counts=letter_counts, rules=rules):
    for i in range(steps):
        new_count = {i:0 for i in pair_counts}
        for k, v in pair_counts.items():
            new_count[rules_pairs[k][0]] += v
            new_count[rules_pairs[k][1]] += v
            letter_counts[rules[k]] += v

        for k in pair_counts:
            pair_counts[k] = new_count[k]


    




def main():
    
    #PART 1
    # final_poly = build_polymer()
    # print(len(final_poly))
    # char_counts = {i : final_poly.count(i) for i in set(final_poly)}
    # print(char_counts)
    # part_1 = max(char_counts.values()) - min(char_counts.values())
    # print(part_1)


    #PART 2
    pair_counting()
    pprint.pprint(letter_counts)
    print(max(letter_counts.values())-min(letter_counts.values()))

   
    


if __name__ == "__main__":
    main()