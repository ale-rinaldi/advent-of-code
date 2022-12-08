with open("d8-input.txt") as f:
    data = f.read().splitlines()

tree_height = {}
matrix_len_y = len(data)
matrix_len_x = len(data[0])
matrix_max_y = matrix_len_y - 1
matrix_max_x = matrix_len_x - 1

for x in range(0, matrix_len_x):
    for y in range(0, matrix_len_y):
        tree_height[(x, y)] = data[y][x]


def visible_from_left(point):
    x = point[0]
    y = point[1]
    target_height = tree_height[(x, y)]
    trees = 0
    while x > 0:
        x -= 1
        if tree_height[(x, y)] >= target_height:
            return trees + 1
        trees += 1
    return trees


def visible_from_right(point):
    x = point[0]
    y = point[1]
    target_height = tree_height[(x, y)]
    trees = 0
    while x < matrix_max_x:
        x += 1
        if tree_height[(x, y)] >= target_height:
            return trees + 1
        trees += 1
    return trees


def visible_from_top(point):
    x = point[0]
    y = point[1]
    target_height = tree_height[(x, y)]
    trees = 0
    while y > 0:
        y -= 1
        if tree_height[(x, y)] >= target_height:
            return trees + 1
        trees += 1
    return trees


def visible_from_bottom(point):
    x = point[0]
    y = point[1]
    target_height = tree_height[(x, y)]
    trees = 0
    while y < matrix_max_y:
        y += 1
        if tree_height[(x, y)] >= target_height:
            return trees + 1
        trees += 1
    return trees


def score(point):
    return visible_from_top(point) * visible_from_bottom(point) * visible_from_left(point) * visible_from_right(point)


scores = []
for x in range(0, matrix_len_x):
    for y in range(0, matrix_len_y):
        scores.append(score((x, y)))

print(max(scores))
