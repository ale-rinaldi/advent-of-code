with open("d1-input.txt") as f:
    data = f.read().splitlines()
elfs = {}
index = 0
for line in data:
    if line == "":
        index += 1
        continue
    if index not in elfs:
        elfs[index] = 0
    elfs[index] += int(line)

values = list(elfs.values())
values.sort(reverse=True)
print(values[0]+values[1]+values[2])
