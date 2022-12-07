with open('d8-input.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def encode_line(line):
    return "\"" + line.replace("\\", "\\\\").replace("\"", "\\\"") + "\""

print(sum([len(encode_line(line)) for line in lines]) - sum([len(line) for line in lines]))
