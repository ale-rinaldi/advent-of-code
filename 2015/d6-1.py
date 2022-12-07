with open('d6-input.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def parse_line(line):
    splitted = line.split(' ')
    if splitted[0] == "toggle":
        return "toggle", splitted[1], splitted[3]
    if splitted[0] == "turn":
        if splitted[1] == "on":
            return "turn on", splitted[2], splitted[4]
        if splitted[1] == "off":
            return "turn off", splitted[2], splitted[4]
    raise ValueError(f"unknown line: {line}")

def parse_matrix(matrix):
    splitted = matrix.split(',')
    return int(splitted[0]), int(splitted[1])

matrix = [[False for _ in range(1000)] for _ in range(1000)]
for line in lines:
    instruction, start_matrix, end_matrix = parse_line(line)
    start_x, start_y = parse_matrix(start_matrix)
    end_x, end_y = parse_matrix(end_matrix)
    if instruction == "turn on":
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                matrix[x][y] = True
    elif instruction == "turn off":
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                matrix[x][y] = False
    elif instruction == "toggle":
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                matrix[x][y] = not matrix[x][y]

print(sum([len([i for i in x if i]) for x in matrix]))