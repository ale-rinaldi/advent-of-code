from astar import AStar

with open("d15-input.txt", "r") as f:
    input_lines = f.readlines()
input_lines = [l.strip() for l in input_lines]

for i, input_line in enumerate(input_lines):
    ints = [int(x) for x in input_line]
    for x in range(0, 4):
        ints = [x + 1 if x < 9 else 1 for x in ints]
        input_lines[i] += "".join([str(i) for i in ints])

new_input_lines = [*input_lines]
for x in range(0, 4):
    for i, line in enumerate(input_lines):
        ints = [int(x) + 1 if int(x) < 9 else 1 for x in input_lines[i]]
        input_lines[i] = ("".join([str(i) for i in ints]))
    new_input_lines += input_lines
input_lines = new_input_lines

matrix_x_len = len(input_lines[0].strip())
matrix_y_len = len(input_lines)
matrix_max_x = matrix_x_len - 1
matrix_max_y = matrix_y_len - 1

matrix = {}
for x in range(0, matrix_x_len):
    for y in range(0, matrix_y_len):
        value = int(input_lines[y][x])
        matrix[(x, y)] = value


def get_neighbors(point):
    neighbors = []
    x = point[0]
    y = point[1]
    if point[0] > 0:
        neighbors.append((x - 1, y))
    if point[0] < matrix_max_x:
        neighbors.append((x + 1, y))
    if point[1] > 0:
        neighbors.append((x, y - 1))
    if point[1] < matrix_max_y:
        neighbors.append((x, y + 1))
    return neighbors


class MyAStar(AStar):
    def neighbors(self, node):
        return get_neighbors(node)

    def distance_between(self, n1, n2) -> float:
        return matrix[n2]

    def heuristic_cost_estimate(self, current, goal) -> float:
        # Returning a random number just elimiates any heuristic, and makes this a Dijkstra
        return 100


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

def print_matrix(matrix, visited=[], current_node=None):
    for y in range(0, matrix_y_len):
        line = ""
        for x in range(0, matrix_max_x+1):
            if (x, y) == current_node:
                line += f"{bcolors.FAIL}{matrix[(x, y)]}{bcolors.ENDC}"
            elif (x, y) in visited:
                line += f"{bcolors.WARNING}{matrix[(x, y)]}{bcolors.ENDC}"
            else:
                line += f"{matrix[(x, y)]}"
        print(line)
    print("")


visited = set()

astar = MyAStar()
result = astar.astar((0, 0), (matrix_max_x, matrix_max_y))
cost = 0

for point in result:
    visited.add(point)
    if point != (0, 0):
        cost += matrix[point]
print_matrix(matrix, visited)
print(cost)
