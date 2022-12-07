import sys

with open('d1-input.txt', 'r') as f:
    content = f.read()

chars = list(content.strip())
floor = 0
pos = 1
for char in chars:
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    if floor == -1:
        print(pos)
        sys.exit(0)
    pos += 1
