with open("d10-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

closings = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points = 0
def assign_points(char):
    global points
    if char == ')':
        points += 3
    elif char == ']':
        points += 57
    elif char == '}':
        points += 1197
    elif char == '>':
        points += 25137

for line in lines:
    stack = []
    for char in list(line):
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        if char in [')', ']', '}', '>']:
            last_stack = stack.pop()
            if closings[last_stack] != char:
                assign_points(char)
                break

print(points)
