with open("d3-input.txt") as f:
    data = f.read().splitlines()

def char_to_int(char):
    if ord(char) >= 41 and ord(char) <= 90:
        return ord(char) - 38
    if ord(char) >= 97 and ord(char) <= 122:
        return ord(char) - 96

res = []
x = 0
current_group = []
for line in data:
    current_group.append(line)
    x+=1
    if x > 2:
        commons = list(set(current_group[0]) & set(current_group[1]) & set(current_group[2]))
        assert len(commons) == 1
        res.append(char_to_int(commons[0]))
        current_group = []
        x = 0
        continue
print(sum(res))
