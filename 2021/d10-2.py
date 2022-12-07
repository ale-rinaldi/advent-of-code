with open("d10-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

closings = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scores = []
def get_points(char):
    global points
    if char == ')':
        return 1
    elif char == ']':
        return 2
    elif char == '}':
        return 3
    elif char == '>':
        return 4
    else:
        raise ValueError(char)

for line in lines:
    stack = []
    invalid = False
    for char in list(line):
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        if char in [')', ']', '}', '>']:
            last_stack = stack.pop()
            if closings[last_stack] != char:
                invalid = True
                break
    if invalid:
        continue
    score = 0
    stack.reverse()
    for char in stack:
        score *= 5
        score += get_points(closings[char])
    scores.append(score)

scores.sort()
print(scores[len(scores) / 2])
