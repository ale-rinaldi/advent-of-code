with open('d2-input.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

res = 0
for line in lines:
    dims = [int(x) for x in line.split('x')]
    sides = [dims[0]*dims[1], dims[0]*dims[2], dims[1]*dims[2]]
    res += 2*sides[0] + 2*sides[1] + 2*sides[2] + min(sides)

print(res)