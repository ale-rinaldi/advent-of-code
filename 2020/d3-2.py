with open("d3-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def check_path(x_shift, y_shift):
    x = 0
    y = 0

    trees = 0
    while y < len(lines):
        if lines[y][x] == '#':
            trees += 1
        y += y_shift
        x = (x + x_shift) % len(lines[0])

    return trees

print(check_path(1, 1) * check_path(3, 1) * check_path(5, 1) * check_path(7, 1) * check_path(1, 2))