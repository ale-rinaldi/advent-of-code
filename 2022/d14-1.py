import os
import time

with open("d14-input.txt") as f:
    data = f.read().splitlines()


class NoSandException(Exception):
    pass


class CannotMoveException(Exception):
    pass


class OverLastRockException(Exception):
    pass


class SandGrid:
    rocks: set
    sand: list
    start_point: tuple
    max_rock_y: int

    def __init__(self):
        self.rocks = set()
        self.sand = []
        self.start_point = (500, 0)
        self.max_rock_y = 0

    def add_rock(self, points: list):
        for i, point in enumerate(points):
            if i == len(points) - 1:
                break
            next_point = points[i + 1]
            if point[0] == next_point[0]:
                min_y = min(point[1], next_point[1])
                max_y = max(point[1], next_point[1])
                for y in range(min_y, max_y + 1):
                    self.rocks.add((point[0], y))
                    self.max_rock_y = max(self.max_rock_y, y)
            elif point[1] == next_point[1]:
                min_x = min(point[0], next_point[0])
                max_x = max(point[0], next_point[0])
                for x in range(min_x, max_x + 1):
                    self.rocks.add((x, point[1]))
                    self.max_rock_y = max(self.max_rock_y, point[1])

    def render(self):
        all_points = set(self.rocks)
        all_points.update(set(self.sand))
        all_points.add(self.start_point)
        min_x = min([p[0] for p in all_points])
        max_x = max([p[0] for p in all_points])
        min_y = min([p[1] for p in all_points])
        max_y = max([p[1] for p in all_points])

        for y in range(min_y, max_y + 1):
            line = ""
            for x in range(min_x, max_x + 1):
                if (x, y) in self.rocks:
                    line += "#"
                elif (x, y) in self.sand:
                    line += "O"
                elif (x, y) == self.start_point:
                    line += "+"
                else:
                    line += "."
            print(line)

    def move_current_sand(self):
        if len(self.sand) == 0:
            raise NoSandException
        x, y = self.sand[-1]
        next_points = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        for point in next_points:
            if point not in self.rocks and point not in self.sand:
                # pos = len(self.sand)-1
                self.sand[-1] = point
                if point[1] >= self.max_rock_y:
                    raise OverLastRockException
                return
        raise CannotMoveException

    def sand_cycle(self):
        try:
            self.move_current_sand()
        except (NoSandException, CannotMoveException):
            self.sand.append(self.start_point)


grid = SandGrid()
for line in data:
    points_str = [p.strip() for p in line.split("->")]
    points = []
    for point in points_str:
        x, y = [int(n) for n in point.split(",")]
        points.append((x, y))
    grid.add_rock(points)

while True:
    try:
        grid.sand_cycle()
    except OverLastRockException:
        break
print(len(grid.sand) - 1)
