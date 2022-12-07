with open("d13-input.txt", "r") as f:
    input_lines = f.readlines()
input_lines = [line.strip() for line in input_lines]


def split_on_empty_line(lines):
    parts = []
    part = []
    for line in lines:
        if line == "":
            if len(part) > 0:
                parts.append(part)
            part = []
            continue
        part.append(line)
    if len(part) > 0:
        parts.append(part)
    return parts


class Grid:
    points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def render(self):
        lines = []
        max_x = max([i[0] for i in self.points])
        max_y = max([i[1] for i in self.points])
        for y in range(0, max_y+1):
            line = []
            for x in range(0, max_x+1):
                if (x, y) in self.points:
                    line.append('#')
                else:
                    line.append('.')
            lines.append("".join(line))
        return "\n".join(lines)

    def fold(self, index, direction):
        if direction == "x":
            max_x = max([i[0] for i in self.points])
            for i, point in enumerate(self.points):
                if point[0] > index:
                    new_x = max_x - point[0]
                    self.points[i] = (new_x, point[1])
        elif direction == "y":
            max_y = max([i[1] for i in self.points])
            for i, point in enumerate(self.points):
                if point[1] > index:
                    new_y = max_y - point[1]
                    self.points[i] = (point[0], new_y)
        self.points = list(set(self.points))

    def count_points(self):
        return len(self.points)

grid = Grid()
parts = split_on_empty_line(input_lines)
points = parts[0]
folds = parts[1]

for point in points:
    (x, y) = point.split(",")
    grid.add_point(int(x), int(y))
print(grid.render())

for i, fold in enumerate(folds):
    fold_parts = fold.split(" ")
    fold_parts = fold_parts[2].split("=")
    grid.fold(int(fold_parts[1]), fold_parts[0])
    print(f"\nAfter fold {i+1}\n")

    print(grid.render())
