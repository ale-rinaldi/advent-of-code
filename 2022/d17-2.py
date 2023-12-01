import math
import os
import time

with open("d17-input.txt") as f:
    data = f.read().splitlines()


class IterativeGetter:
    def __init__(self, elements):
        self.pattern = elements
        self.current_index = 0

    def get(self):
        current = self.pattern[self.current_index]
        self.current_index += 1
        if self.current_index >= len(self.pattern):
            self.current_index = 0
        return current


jet = IterativeGetter(data[0])
pieces = IterativeGetter([1, 2, 3, 4, 5])


def new_piece(higher_y):
    piece = pieces.get()
    base_x = 2
    base_y = higher_y + 3
    if piece == 1:
        return {(base_x, base_y), (base_x + 1, base_y), (base_x + 2, base_y), (base_x + 3, base_y)}
    if piece == 2:
        return {(base_x + 1, base_y), (base_x, base_y + 1), (base_x + 1, base_y + 1), (base_x + 2, base_y + 1),
                (base_x + 1, base_y + 2)}
    if piece == 3:
        return {(base_x, base_y), (base_x + 1, base_y), (base_x + 2, base_y), (base_x + 2, base_y + 1),
                (base_x + 2, base_y + 2)}
    if piece == 4:
        return {(base_x, base_y), (base_x, base_y + 1), (base_x, base_y + 2), (base_x, base_y + 3)}
    if piece == 5:
        return {(base_x, base_y), (base_x + 1, base_y), (base_x, base_y + 1), (base_x + 1, base_y + 1)}
    raise Exception(f"Unknown piece type {piece}")


class Grid:
    fallen_pieces: int
    fallen_points: set
    current_piece: set
    fallen_max_y: int
    max_y: int
    max_x: int

    def __init__(self):
        self.fallen_points = set()
        self.fallen_pieces = 0
        self.current_piece = new_piece(0)
        self.fallen_max_y = 0
        self.max_y = max([p[1] for p in self.current_piece])
        self.max_x = 6

    def fallen_max_y(self):
        return max([point[1] for point in self.fallen_points])

    def current_piece_fallen(self):
        for point in self.current_piece:
            if point[1] == 0:
                return True
            if (point[0], point[1] - 1) in self.fallen_points:
                return True
        return False

    def render(self):
        os.system("clear")
        for rev_y in range(0, self.max_y + 1):
            y = self.max_y - rev_y
            line = ""
            for x in range(0, self.max_x + 1):
                if (x, y) in self.current_piece:
                    line += "@"
                elif (x, y) in self.fallen_points:
                    line += "#"
                else:
                    line += "."
            print(line)

    def move_right(self):
        for p in self.current_piece:
            if p[0] == self.max_x or (p[0]+1, p[1]) in self.fallen_points:
                return
        self.current_piece = set([(p[0] + 1, p[1]) for p in self.current_piece])

    def move_left(self):
        for p in self.current_piece:
            if p[0] == 0 or (p[0]-1, p[1]) in self.fallen_points:
                return
        self.current_piece = set([(p[0] - 1, p[1]) for p in self.current_piece])

    def check_fallen(self):
        if self.current_piece_fallen():
            self.fallen_points.update(self.current_piece)
            self.fallen_max_y = max(self.fallen_max_y, max([p[1] for p in self.current_piece]))
            self.fallen_pieces += 1
            self.current_piece = new_piece(self.fallen_max_y + 1)
            self.max_y = max([p[1] for p in self.current_piece])
            return True
        return False

    def fall(self):
        if not self.check_fallen():
            self.current_piece = set([(p[0], p[1] - 1) for p in self.current_piece])

    def do_movement(self):
        movement = jet.get()
        if movement == ">":
            self.move_right()
        elif movement == "<":
            self.move_left()
        else:
            raise Exception(f"unknown movement: {movement}")


grid = Grid()

repetition_point = math.lcm(5, len(data[0]))
necessary_repetitions = 1000000000000 // repetition_point
missing_ones = 1000000000000 % repetition_point

while grid.fallen_pieces < repetition_point:
    os.system("clear")
    grid.render()
    time.sleep(0.1)
    grid.do_movement()
    os.system("clear")
    grid.render()
    time.sleep(0.1)
    grid.fall()

height_so_far = grid.fallen_max_y

while grid.fallen_pieces < repetition_point + missing_ones:
    grid.do_movement()
    grid.fall()

missing_height = grid.fallen_max_y - height_so_far

print(height_so_far*necessary_repetitions + missing_height)