with open("d8-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

count = 0
for line in lines:
    parts = line.split(" | ")
    outputs = parts[1].split(" ")
    count += len([x for x in outputs if len(x) in [2, 4, 3, 7]])

print(count)
