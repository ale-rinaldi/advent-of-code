with open("d11-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

matrix = [[int(x) for x in list(l)] for l in lines]

def print_matrix():
    for row in matrix:
        if row[0] < 10:
            string = f" {row[0]}"
        else:
            string =f"{row[0]}"
        for y in range(1, len(row)):
            if row[y] < 10:
                string = f"{string}  {row[y]}"
            else:
                string = f"{string} {row[y]}"
        print(string)

def step():
    flashes = 0
    flashed = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] += 1
    while len([x for x in sum(matrix, []) if x > 9]) > 0:
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] < 10:
                    continue
                matrix[x][y] = 0
                flashes += 1
                flashed.append((x, y))
                if x>0 and y>0 and (x-1, y-1) not in flashed:
                    matrix[x-1][y-1] +=1
                if x > 0 and (x-1, y) not in flashed:
                    matrix[x-1][y] += 1
                if x > 0 and y < len(matrix[x]) - 1 and (x-1, y+1) not in flashed:
                    matrix[x-1][y+1] += 1
                if y < len(matrix[x]) - 1 and (x, y+1) not in flashed:
                    matrix[x][y+1] += 1
                if x < len(matrix) - 1 and y < len(matrix[x]) - 1 and (x+1, y+1) not in flashed:
                    matrix[x+1][y+1] += 1
                if x < len(matrix) - 1 and (x+1, y) not in flashed:
                    matrix[x+1][y] += 1
                if x < len(matrix) - 1 and y > 0 and (x+1, y-1) not in flashed:
                    matrix[x+1][y-1] += 1
                if y > 0 and (x, y-1) not in flashed:
                    matrix[x][y-1] += 1
    return flashes

step_num = 0
while True:
    step_num += 1
    flashes = step()
    if flashes == len(matrix) * len(matrix[0]):
        print(step_num)
        break
