import pprint

example_input = ".venv/advent_9_example.txt"
input = ".venv/advent_9_input.txt"
with open(input) as file:
    heightmap =  file.read().splitlines()
    for index, item in enumerate(heightmap):
             heightmap[index] = [int(j) for j in item]

nines_heightmap = heightmap
for i in heightmap:
    i.insert(0,9)
    i.append(9)
nines_heightmap.insert(0, [9 for j in nines_heightmap[0]])
nines_heightmap.append([9 for j in nines_heightmap[0]])
# pprint.pprint(nines_heightmap)

def local_min(heightmap):
    minima = []
    for index, item in enumerate(heightmap):
        if index == 0:
            for i, j in enumerate(item):
                if i == 0: 
                    if j <  min([item[1], heightmap[index+1][0]]):
                        minima.append(j)
                elif i == len(item)-1:
                    if j <  min([item[i-1], heightmap[index+1][i]]):
                        minima.append(j)
                else:
                    if j < min([item[i-1],item[i+1], heightmap[index+1][i]]):
                        minima.append(j)
        elif index == len(heightmap)-1:
            for i, j in enumerate(item):
                if i == 0: 
                    if j <  min([item[i+1], heightmap[index-1][i]]):
                        minima.append(j)
                elif i == len(item)-1:
                    if j <  min([item[i-1], heightmap[index-1][i]]):
                        minima.append(j)
                else:
                    if j < min([item[i-1], item[i+1], heightmap[index-1][i]]):
                        minima.append(j)
        else:
            for i , j in enumerate(item):
                if i == 0: 
                    if j <  min([item[1], heightmap[index-1][0], heightmap[index+1][0]]):
                        minima.append(j)
                elif i == len(item)-1:
                    if j <  min([item[i-1], heightmap[index+1][i], heightmap[index-1][i]]):
                        minima.append(j)
                else:
                    if j < min([item[i-1], item[i+1], heightmap[index+1][i], heightmap[index-1][i]]):
                        minima.append(j)
    return minima

def local_min_nines(heightmap):
    minima = []
    for index, item in enumerate(heightmap):
        if index > 0 and index < len(heightmap)-1:
            for i, j in enumerate(item):
                if i > 0 and i < len(item) - 1: 
                    if j <  min([item[i-1], item[i+1], heightmap[index+1][i], heightmap[index-1][i]]):
                        minima.append((j, (index, i)))
    return minima

def bfs(node,heightmap):
    visited = True
    graph = {f"{node}": True}
    queue = [node]


    while queue:
        current = queue.pop()
        # print(current)
        current_row = current[0]
        current_col = current[1]
        up = (current_row-1, current_col)
        down = (current_row+1, current_col)
        left = (current_row, current_col-1)
        right = (current_row, current_col+1)
        up_val = heightmap[current_row -1][current_col]
        down_val = heightmap[current_row +1][current_col]
        left_val = heightmap[current_row][current_col-1]
        right_val = heightmap[current_row][current_col+1]
        if up_val != 9 and f"{up}" not in graph:
            queue.append(up)
            graph[f"{up}"] = True
        if down_val != 9 and f"{down}" not in graph:
            queue.append(down)
            graph[f"{down}"] = True
        if left_val != 9 and f"{left}" not in graph:
            queue.append(left)
            graph[f"{left}"] = True
        if right_val != 9 and f"{right}" not in graph:
            queue.append(right)
            graph[f"{right}"] = True
    
    basin_size = len(graph.keys())
    return basin_size
        




def main():
    # minima = local_min(heightmap)
    nines_minima = local_min_nines(nines_heightmap)
    # print(nines_minima) 
    minima_locations = [i[1] for i in nines_minima]
    basins = [bfs(i,nines_heightmap) for i in minima_locations]
    print(basins)
    sorted_basins = sorted(basins)
    print(sorted_basins[-1]*sorted_basins[-2]*sorted_basins[-3])
    # nodes = [i[0] for i in nines_minima]
    # print(nodes)
    # print(sum(nodes) + len(nodes)) 
    # print(sum(minima) + len(minima))   


if __name__ == "__main__":
    main()

# pprint.pprint(heightmap)   
   