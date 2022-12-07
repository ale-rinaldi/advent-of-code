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
    cur_x = x1
    cur_y = y1
    dst_x = x2
    dst_y = y2
    grid_increment(cur_x, cur_y)
    while cur_x != dst_x or cur_y != dst_y:
        if cur_x < dst_x:
            cur_x += 1
        elif cur_x > dst_x:
            cur_x -= 1
        if cur_y < dst_y:
            cur_y += 1
        elif cur_y > dst_y:
            cur_y -= 1
        grid_increment(cur_x, cur_y)

res = 0
for x, line in grid.items():
    for y, item in line.items():
        if item > 1:
            res += 1

print(res)
