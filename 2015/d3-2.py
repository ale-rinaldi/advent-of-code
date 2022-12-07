with open('d3-input.txt', 'r') as f:
    content = f.read()

chars = list(content.strip())

visited = []

x1 = 0
y1 = 0
x2 = 0
y2 = 0
visited.append((0, 0))
for i, char in enumerate(chars):
    if i % 2 == 0:
        if char == '^':
            y1 += 1
        elif char == 'v':
            y1 -= 1
        elif char == '>':
            x1 += 1
        elif char == '<':
            x1 -= 1
        visited.append((x1, y1))
    else:
        if char == '^':
            y2 += 1
        elif char == 'v':
            y2 -= 1
        elif char == '>':
            x2 += 1
        elif char == '<':
            x2 -= 1
        visited.append((x2, y2))

print(len(set(visited)))
