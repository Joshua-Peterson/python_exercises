import re
import pprint

example_input = ".venv/advent_5_example.txt"
input = ".venv/advent_5_input.txt"
with open(input) as file:
    data =  file.read()

# prog = re.compile(r"(\b\d+,\d+\b)+")
# result = prog.findall(data)
# result = [eval(i) for i in result]

prog = re.compile(r"(\b\d+\b)+")
result = prog.findall(data)
result = [int(i) for i in result]

grid_size = [max(result[0:len(result):2]), max(result[1:len(result):2])]
points_list = [tuple(result[i:i+2]) for i in range(0,len(result),2)]
line_seg_list = [points_list[i:i+2] for i in range(0, len(points_list),2)]
horiz_vert_segments = [seg for seg in line_seg_list if seg[0][0] == seg[1][0] or seg[0][1] == seg[1][1]]
print(grid_size)
# pprint.pprint(line_seg_list)
# pprint.pprint(horiz_vert_segments)
def count_amount(point, li, num=2):
    counter = 0
    for i in li:
        if i == point:
            counter += 1
        if counter == num:
            return True
    return False
        

def points_on_line(segment):
    x_coords = [segment[0][0], segment[1][0]]
    y_coords = [segment[0][1], segment[1][1]]
    points = []
    if x_coords[0] == x_coords[1]:
        for y in range(min(y_coords),max(y_coords)+1):
            point = (x_coords[0], y)
            points.append(point)
    else:
        slope = (y_coords[1]-y_coords[0])/(x_coords[1]-x_coords[0])
        intercept = y_coords[0] - int(slope * x_coords[0]) 
        for x in range(min(x_coords), max(x_coords)+1):
            point = (x, int(slope*x)+ intercept)
            points.append(point)
    return points


points = []
for segment in line_seg_list:
    points += points_on_line(segment)
# pprint.pprint(points)
# tot = 0
unique_points = list(set(points))
for i in unique_points:
    points.remove(i)
# pprint.pprint(unique_points)
uniqier = list(set(points))
print(len(uniqier))
#     if count_amount(i,points):
#         tot += 1
# print(tot)


# intersections = {i:points.count(i) for i in unique_points}
# print(sum(1 if i >= 2 else 0 for i in intersections.values()))

# line_intersections = [print(points.count(i)) for i in points]
# pprint.pprint(line_intersections)
# print(sum(1 if i >= 2 else 0 for i in line_intersections))
    