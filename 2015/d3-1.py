with open('d3-input.txt', 'r') as f:
    content = f.read()

chars = list(content.strip())

visited = []

x = 0
y = 0
visited.append((x, y))
for char in chars:
    if char == '^':
        y += 1
    elif char == 'v':
        y -= 1
    elif char == '>':
        x += 1
    elif char == '<':
        x -= 1
    visited.append((x, y))

print(len(set(visited)))
