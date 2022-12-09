with open("d9-input.txt") as f:
    data = f.read().splitlines()


class Rope:
    def __init__(self):
        self.head = (0, 0)
        self.tail = (0, 0)
        self.tail_visited = set()

    def tail_is_adjacent(self):
        if self.head == self.tail:
            return True
        if self.head == (self.tail[0] + 1, self.tail[1]):
            return True
        if self.head == (self.tail[0] - 1, self.tail[1]):
            return True
        if self.head == (self.tail[0], self.tail[1] + 1):
            return True
        if self.head == (self.tail[0], self.tail[1] - 1):
            return True
        if self.head == (self.tail[0] + 1, self.tail[1] + 1):
            return True
        if self.head == (self.tail[0] - 1, self.tail[1] - 1):
            return True
        if self.head == (self.tail[0] + 1, self.tail[1] - 1):
            return True
        if self.head == (self.tail[0] - 1, self.tail[1] + 1):
            return True

    def follow_head(self):
        if self.tail_is_adjacent():
            return
        if self.head[1] == self.tail[1]:
            x_shift = 1 if self.head[0] > self.tail[0] else -1
            y_shift = 0
        elif self.head[0] == self.tail[0]:
            x_shift = 0
            y_shift = 1 if self.head[1] > self.tail[1] else -1
        else:
            x_shift = 1 if self.head[0] > self.tail[0] else -1
            y_shift = 1 if self.head[1] > self.tail[1] else -1
        self.tail = (self.tail[0] + x_shift, self.tail[1] + y_shift)

    def move_head(self, x_shift: int, y_shift: int):
        if abs(x_shift) > 1 or abs(y_shift) > 1:
            raise Exception("cannot move more than one")
        if x_shift != 0 and y_shift != 0:
            raise Exception("cannot move both axis")
        self.head = (self.head[0] + x_shift, self.head[1] + y_shift)
        self.follow_head()
        self.tail_visited.add(self.tail)

    def move_right(self, num):
        for _ in range(0, num):
            self.move_head(1, 0)

    def move_left(self, num):
        for _ in range(0, num):
            self.move_head(-1, 0)

    def move_up(self, num):
        for _ in range(0, num):
            self.move_head(0, -1)

    def move_down(self, num):
        for _ in range(0, num):
            self.move_head(0, 1)

    def render(self):
        matrix_x_min_boundary = min([self.head[0], self.tail[0], 0])
        matrix_x_max_boundary = max([self.head[0], self.tail[0], 0])
        matrix_y_min_boundary = min([self.head[1], self.tail[1], 0])
        matrix_y_max_boundary = max([self.head[1], self.tail[1], 0])

        for y in range(matrix_y_min_boundary, matrix_y_max_boundary + 1):
            line = ""
            for x in range(matrix_x_min_boundary, matrix_x_max_boundary + 1):
                char = "."
                if self.head == (x, y):
                    char = "H"
                if self.tail == (x, y) and self.tail != self.head:
                    char = "T"
                if (x, y) == (0, 0) and self.head != (0, 0) and self.tail != (0, 0):
                    char = "s"
                line += char
            print("".join(line))

    def render_visited_matrix(self):
        matrix_x_min_boundary = min([p[0] for p in self.tail_visited])
        matrix_x_max_boundary = max([p[0] for p in self.tail_visited])
        matrix_y_min_boundary = min([p[1] for p in self.tail_visited])
        matrix_y_max_boundary = max([p[1] for p in self.tail_visited])

        for y in range(matrix_y_min_boundary, matrix_y_max_boundary + 1):
            line = ""
            for x in range(matrix_x_min_boundary, matrix_x_max_boundary + 1):
                line += "#" if (x, y) in self.tail_visited else "."
            print(line)


rope = Rope()
for line in data:
    splitted = line.split(" ")
    direction = splitted[0]
    number = int(splitted[1])

    if direction == "L":
        rope.move_left(number)
    elif direction == "R":
        rope.move_right(number)
    elif direction == "U":
        rope.move_up(number)
    elif direction == "D":
        rope.move_down(number)
    else:
        raise Exception("unknown direction")

print(len(rope.tail_visited))
