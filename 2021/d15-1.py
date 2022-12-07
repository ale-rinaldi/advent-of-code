import os
import sys

with open("d15-input.txt", "r") as f:
    input_lines = f.readlines()

matrix_x_len = len(input_lines[0].strip())
matrix_y_len = len(input_lines)
matrix_max_x = matrix_x_len-1
matrix_max_y = matrix_y_len-1

matrix = {}
for x in range(0, matrix_x_len):
    for y in range(0, matrix_y_len):
        value = int(input_lines[y][x])
        matrix[(x, y)] = value

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_matrix(matrix, unvisited=[], current_node=None):
    for y in range(0, matrix_y_len):
        line = ""
        for x in range(0, matrix_max_x+1):
            if (x, y) == current_node:
                line += f"{bcolors.FAIL}{matrix[(x, y)]}{bcolors.ENDC}"
            elif (x, y) not in unvisited:
                line += f"{bcolors.WARNING}{matrix[(x, y)]}{bcolors.ENDC}"
            else:
                line += f"{matrix[(x, y)]}"
        print(line)
    print("")



unvisited = set()
tentative_distance = {}
current_node = (0, 0)
destination_node = (matrix_max_x, matrix_max_y)


def get_unvisited_neighbors(point):
    neighbors = []
    x = point[0]
    y = point[1]
    if point[0] > 0 and (x-1, y) in unvisited:
        neighbors.append((x-1, y))
    if point[0] < matrix_max_x and (x+1, y) in unvisited:
        neighbors.append((x+1, y))
    if point[1] > 0 and (x, y-1) in unvisited:
        neighbors.append((x, y-1))
    if point[1] < matrix_max_y and (x, y+1) in unvisited:
        neighbors.append((x, y+1))
    return neighbors


def is_less(new, current):
    if current is None:
        return True
    return new < current


def is_finished():
    if current_node == (0, 0):
        return False
    if destination_node not in unvisited:
        return True
    for node in list(unvisited):
        if tentative_distance[node] is not None:
            return False
    return True


for x in range(0, matrix_x_len):
    for y in range(0, matrix_y_len):
        unvisited.add((x, y))
        tentative_distance[(x, y)] = None
tentative_distance[(0, 0)] = 0

while not is_finished():
    neighbors = get_unvisited_neighbors(current_node)
    for neighbor in neighbors:
        distance = tentative_distance[current_node] + matrix[neighbor]
        if is_less(distance, tentative_distance[neighbor]):
            tentative_distance[neighbor] = distance
    unvisited.remove(current_node)
    next_node = None
    for node in unvisited:
        if tentative_distance[node] is not None and (next_node is None or tentative_distance[node] < tentative_distance[next_node]):
            next_node = node
    current_node = next_node
    print("Missing to visit: ", len(list(unvisited)))

print(tentative_distance[destination_node])
