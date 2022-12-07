with open("d5-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

grid = {}

def grid_increment(x, y):
    if x not in grid:
        grid[x] = {}
    if y not in grid[x]:
        grid[x][y] = 0
    grid[x][y] += 1

def grid_get(x, y):
    if x not in grid:
        return 0
    if y not in grid[x]:
        return 0
    return grid[x][y]

for line in lines:
    line_arr = line.split(' -> ')
    split1 = line_arr[0].split(',')
    x1 = int(split1[0])
    y1 = int(split1[1])
    split2 = line_arr[1].split(',')
    x2 = int(split2[0])
    y2 = int(split2[1])
    if x1 != x2 and y1 != y2:
        continue
    if x1 == x2:
        if y1 > y2:
            swap = y1
            y1 = y2
            y2 = swap
        for y in range(y1, y2+1):
            grid_increment(x1, y)
    elif y1 == y2:
        if x1 > x2:
            swap = x1
            x1 = x2
            x2 = swap
        for x in range(x1, x2+1):
            grid_increment(x, y1)

res = 0
for x, line in grid.items():
    for y, item in line.items():
        if item > 1:
            res += 1

print(res)
