with open('d8-input.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def parse_line(line):
    res = []
    i = 0
    while i < len(line):
        char = line[i]
        if char == "\"":
            i += 1
            continue
        elif char == "\\":
            if line[i+1] == "\\":
                res.append("\\")
                i += 2
                continue
            elif line[i+1] == "\"":
                res.append("\"")
                i += 2
                continue
            elif line[i+1] == "x":
                res.append("X")
                i += 4
                continue
            else:
                raise ValueError(line[i+1])
        else:
            res.append(char)
            i += 1
    return "".join(res)

print(sum([len(line) for line in lines]) - sum([len(parse_line(line)) for line in lines]))
