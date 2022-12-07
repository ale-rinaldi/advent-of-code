with open("d7-input.txt", "r") as f:
    content = f.read()

positions = [int(x.strip()) for x in content.strip().split(",")]

min_pos = min(positions)
max_pos = max(positions)

result = {}

for x in range(min_pos, max_pos):
    fuel = 0
    for crab in positions:
        shift = abs(crab-x)
        fuel += sum(range(1, shift+1))
    result[x] = fuel

pos=None
val=None
for k, v in result.items():
    if val is None or val > v:
        val = v
        pos = k

print(val, pos)
