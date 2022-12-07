with open("d3-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

x = 0
y = 0

trees = 0
while y < len(lines):
    if lines[y][x] == '#':
        trees += 1
    y += 1
    x = (x + 3) % len(lines[0])

print(trees)
