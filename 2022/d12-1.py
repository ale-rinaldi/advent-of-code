from astar import AStar

with open("d12-input.txt") as f:
    data = f.read().splitlines()

points = {}
start_point = None
end_point = None

len_y = len(data)
len_x = len(data[0])
max_y = len_y - 1
max_x = len_x - 1

for y in range(0, len_y):
    for x in range(0, len_x):
        point_value = data[y][x]
        if point_value == "S":
            start_point = (x, y)
            points[(x, y)] = ord('a')
        elif point_value == "E":
            end_point = (x, y)
            points[(x, y)] = ord('z')
        else:
            points[(x, y)] = ord(point_value)


class MyAStar(AStar):
    def neighbors(self, node):
        result = []
        neighbors = [(node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)]

        for neighbor in neighbors:
            if neighbor in points and points[neighbor] <= points[node]+1:
                result.append(neighbor)

        return result

    def distance_between(self, n1, n2) -> float:
        return 1

    def heuristic_cost_estimate(self, current, goal) -> float:
        # Returning a random number just eliminates any heuristic, and makes this a Dijkstra
        return 100


myastar = MyAStar()
solution = myastar.astar(start_point, end_point)
print(len(list(solution))-1)
