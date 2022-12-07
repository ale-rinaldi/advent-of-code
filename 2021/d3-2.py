with open('d3-input.txt', 'r') as file:
    lines = file.readlines()

def find_most_common(bytes):
    zeros = len([x for x in bytes if x == "0"])
    ones = len([x for x in bytes if x == "1"])
    if zeros > ones:
        return "0"
    else:
        return "1"

def find_least_common(bytes):
    zeros = len([x for x in bytes if x == "0"])
    ones = len([x for x in bytes if x == "1"])
    if zeros <= ones:
        return "0"
    else:
        return "1"

items = [x.strip() for x in lines]
oxygen = None
for i, _ in enumerate(lines[0].strip()):
    common = find_most_common([x[i] for x in items])
    items = [x for x in items if x[i] == common]
    if len(items) == 1:
        oxygen = int(items[0], 2)
        break

items = [x.strip() for x in lines]
co2 = None
for i, _ in enumerate(lines[0].strip()):
    common = find_least_common([x[i] for x in items])
    items = [x for x in items if x[i] == common]
    if len(items) == 1:
        co2 = int(items[0], 2)
        break

print(oxygen*co2)
