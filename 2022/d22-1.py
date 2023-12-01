import os
import time

EMPTY = " "
FREE = "."
WALL = "#"


class Grid:
    points: dict
    max_x: int
    max_y: int
    x_min_points: dict
    x_max_points: dict
    y_min_points: dict
    y_max_points: dict
    current_point_x: int
    current_point_y: int
    current_direction: int

    def __init__(self, data):
        self.points = {}
        self.max_x = 0
        self.max_y = 0
        self.x_min_points = {}
        self.x_max_points = {}
        self.y_min_points = {}
        self.y_max_points = {}
        self.current_direction = 0

        for y, line in enumerate(data):
            for x, char in enumerate(line):
                self.set_point(x, y, char)

        self.current_point_x = self.x_min_points[0]
        self.current_point_y = 0

    def set_point(self, x, y, value):
        if value == EMPTY:
            return
        if x not in self.points:
            self.points[x] = {}
        self.points[x][y] = value
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y
        if y not in self.x_min_points or self.x_min_points[y] > x:
            self.x_min_points[y] = x
        if y not in self.x_max_points or self.x_max_points[y] < x:
            self.x_max_points[y] = x
        if x not in self.y_min_points or self.y_min_points[x] > y:
            self.y_min_points[x] = y
        if x not in self.y_max_points or self.y_max_points[x] < y:
            self.y_max_points[x] = y

    def get_point(self, x, y):
        if x not in self.points:
            return EMPTY
        if y not in self.points[x]:
            return EMPTY
        return self.points[x][y]

    def turn(self, direction):
        if direction == "R":
            self.current_direction += 1
            if self.current_direction > 3:
                self.current_direction = 0
        elif direction == "L":
            self.current_direction -= 1
            if self.current_direction < 0:
                self.current_direction = 3
        else:
            raise Exception("invalid turn direction")

    def move(self):
        if self.current_direction == 0:
            candidate_point_x, candidate_point_y = self.current_point_x + 1, self.current_point_y
            if self.get_point(candidate_point_x, candidate_point_y) == EMPTY:
                candidate_point_x = self.x_min_points[candidate_point_y]
        elif self.current_direction == 1:
            candidate_point_x, candidate_point_y = self.current_point_x, self.current_point_y + 1
            if self.get_point(candidate_point_x, candidate_point_y) == EMPTY:
                candidate_point_y = self.y_min_points[candidate_point_x]
        elif self.current_direction == 2:
            candidate_point_x, candidate_point_y = self.current_point_x - 1, self.current_point_y
            if self.get_point(candidate_point_x, candidate_point_y) == EMPTY:
                candidate_point_x = self.x_max_points[candidate_point_y]
        elif self.current_direction == 3:
            candidate_point_x, candidate_point_y = self.current_point_x, self.current_point_y - 1
            if self.get_point(candidate_point_x, candidate_point_y) == EMPTY:
                candidate_point_y = self.y_max_points[candidate_point_x]
        else:
            raise Exception(f"Invalid current direction {self.current_direction}")
        if self.get_point(candidate_point_x, candidate_point_y) == WALL:
            return
        self.current_point_x, self.current_point_y = candidate_point_x, candidate_point_y

    def render(self):
        for y in range(self.max_y + 1):
            line = ""
            for x in range(self.max_x + 1):
                if self.current_point_x == x and self.current_point_y == y:
                    line += "C"
                else:
                    line += self.get_point(x, y)
            print(line)


def parse_directions(directions):
    result = []
    current_number = 0
    for char in directions:
        if char in ["R", "L"]:
            if current_number > 0:
                result.append(current_number)
            result.append(char)
            current_number = 0
            continue
        number = int(char)
        current_number = current_number * 10 + number
    if current_number > 0:
        result.append(current_number)
    return result


with open("d22-input.txt") as f:
    data = f.read()
grid_data, directions = data.split("\n\n")
grid_data = grid_data.splitlines()

grid = Grid(grid_data)

directions = parse_directions(directions)
for direction in directions:
    if direction in ["L", "R"]:
        grid.turn(direction)
    else:
        for _ in range(direction):
            grid.move()

print((grid.current_point_y+1) * 1000 + (grid.current_point_x+1) * 4 + grid.current_direction)
