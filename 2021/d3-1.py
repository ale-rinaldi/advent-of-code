with open('d3-input.txt', 'r') as file:
    lines = file.readlines()

bytes = []
for i, _ in enumerate(lines[0].strip()):
    if len([x[i] for x in lines if x[i] == '1']) > len([x[i] for x in lines if x[i] == '0']):
        bytes.append("1")
    else:
        bytes.append("0")

gamma = int(''.join(bytes), 2)

bytes = []
for i, _ in enumerate(lines[0].strip()):
    if len([x[i] for x in lines if x[i] == '1']) < len([x[i] for x in lines if x[i] == '0']):
        bytes.append("1")
    else:
        bytes.append("0")

epsilon = int(''.join(bytes), 2)

print(gamma*epsilon)
