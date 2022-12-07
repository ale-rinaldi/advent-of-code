import sys

with open("d1-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

for i, line in enumerate(lines):
    for j, line in enumerate(lines):
        for k, line in enumerate(lines):
            if i == j or i == k or j == k:
                continue
            n1 = int(lines[i])
            n2 = int(lines[j])
            n3 = int(lines[k])
            if n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
                sys.exit(0)
