# I'm a bad person, I had a look at https://github.com/gwpmad/advent-of-code-2021/blob/main/14/main.go
with open("d14-input.txt", "r") as f:
    input_lines = f.readlines()
input_lines = [line.strip() for line in input_lines]


def split_on_empty_line(lines):
    parts = []
    part = []
    for line in lines:
        if line == "":
            if len(part) > 0:
                parts.append(part)
            part = []
            continue
        part.append(line)
    if len(part) > 0:
        parts.append(part)
    return parts


class Counter:
    def __init__(self):
        self.counter = {}
    def incr(self, key, amount=1):
        if key not in self.counter:
            self.counter[key] = 0
        self.counter[key] += amount
    def items(self):
        return self.counter.items()
    def values(self):
        return self.counter.values()
    def clone(self):
        new = Counter()
        new.counter = {**self.counter}
        return new


(start_polymer, raw_rules) = split_on_empty_line(input_lines)
start_polymer = start_polymer[0]
rules = {}
for rule in raw_rules:
    split_rule = rule.split(' -> ')
    rules[split_rule[0]] = split_rule[1]

pairs_count = Counter()
chars_count = Counter()
for x in range(0, len(start_polymer)-1):
    pair = f"{start_polymer[x]}{start_polymer[x+1]}"
    pairs_count.incr(pair)
    chars_count.incr(start_polymer[x])
chars_count.incr(start_polymer[-1])

for iteration in range(0, 40):
    new_count = pairs_count.clone()
    for pair, occurrences in pairs_count.items():
        if occurrences < 1:
            continue
        if pair not in rules:
            continue
        new_pair_1 = f"{pair[0]}{rules[pair]}"
        new_pair_2 = f"{rules[pair]}{pair[1]}"
        new_count.incr(pair, -occurrences)
        new_count.incr(new_pair_1, occurrences)
        new_count.incr(new_pair_2, occurrences)
        chars_count.incr(rules[pair], occurrences)
    pairs_count = new_count

values = chars_count.values()
print(max(values) - min(values))
