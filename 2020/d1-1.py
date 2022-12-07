import sys

with open("d1-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

for i, line in enumerate(lines):
    for j, line in enumerate(lines):
        if i == j:
            continue
        n1 = int(lines[i])
        n2 = int(lines[j])
        if n1 + n2 == 2020:
            print(n1 * n2)
            sys.exit(0)
