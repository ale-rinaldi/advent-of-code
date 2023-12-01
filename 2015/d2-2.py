    with open('d2-input.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

res = 0
for line in lines:
    dims = [int(x) for x in line.split('x')]
    dims.sort()
    res += 2*dims[0] + 2*dims[1] + dims[0]*dims[1]*dims[2]

print(res)