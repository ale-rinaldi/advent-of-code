with open("d9-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

matrix = [[int(x) for x in line] for line in lines]

def is_lowest(matrix, x, y):
    adjacents = []
    if y != 0:
        adjacents.append(matrix[x][y-1])
    if y != len(matrix[x]) -1:
        adjacents.append(matrix[x][y+1])
    if x != 0:
        adjacents.append(matrix[x-1][y])
    if x != len(matrix) -1:
        adjacents.append(matrix[x+1][y])
    return min(adjacents) > matrix[x][y]

risk = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if is_lowest(matrix, x, y):
            risk += (matrix[x][y] + 1)
print(risk)
