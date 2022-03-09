import pprint

example_input = ".venv/advent_12_example.txt"
input = ".venv/advent_12_input.txt"

with open(input) as file:
    caves =  file.read().splitlines()
    
graph = {}
for index, item, in enumerate(caves):
    caves[index] = item.split('-')
for cave in caves:
    if cave[0] not in graph:
        graph[cave[0]]= [cave[1]]
    else:
        graph[cave[0]].append(cave[1])
    if cave[1] not in graph:
        graph[cave[1]] = [cave[0]]
    else: 
        graph[cave[1]].append(cave[0])

small_caves = [i for i in graph if i.islower() and (i != 'start' and i != 'end')]

# paths = []
# def dfs(graph=graph, paths=paths):
#     path = []
#     visited = {cave: False for cave in graph}
#     stack = []
#     current = 'start'
#     stack.append(current)

#     while stack:
#         current = stack.pop()
#         # pathss = [[current, i] for i in graph[current] if i]
#         if current == 'end':
#             path.append(current)
#             paths.append(path)
#             path = ['start']
#         elif not(visited[current]) or current.isupper(): 
#             path.append(current)
#             visited[current] = True
#             stack.extend(graph[current])
    
def find_all_paths(graph=graph, start='start', end='end', path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for cave in graph[start]:
        if cave not in path or cave.isupper():
            newpaths = find_all_paths(graph, cave, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_all_paths_part2(graph=graph, start='start', end='end', path=[], double_cave=''):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for cave in graph[start]:
        if cave not in path or cave.isupper() or (cave == double_cave and path.count(cave) < 2):
            newpaths = find_all_paths_part2(graph, cave, end, path, double_cave)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


pprint.pprint(graph)


def main():
#PART 1 
    # dfs()
    # print(paths)
    paths = find_all_paths()
    # print(len(paths))

# PART 2
    paths_2 = set()
    for small_cave in small_caves:
        pths = find_all_paths_part2(graph,'start','end', [], small_cave)
        for i in pths:
            paths_2.add(tuple(i))
    

    # pprint.pprint(paths_2)
    print(len(paths_2))


if __name__ == "__main__":
    main()

