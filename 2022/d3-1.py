with open("d3-input.txt") as f:
    data = f.read().splitlines()

def char_to_int(char):
    if ord(char) >= 41 and ord(char) <= 90:
        return ord(char) - 38
    if ord(char) >= 97 and ord(char) <= 122:
        return ord(char) - 96

res = []
for line in data:
    length = len(line)
    first_half = line[:int(length/2)]
    second_half = line[int(length/2):]
    common = list(set(list(first_half)) & set(list(second_half)))
    res.append(char_to_int(common[0]))
print(sum(res))
