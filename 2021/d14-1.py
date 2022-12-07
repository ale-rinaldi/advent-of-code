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


(start_polymer, raw_rules) = split_on_empty_line(input_lines)
start_polymer = start_polymer[0]
rules = {}
for rule in raw_rules:
    split_rule = rule.split(' -> ')
    rules[split_rule[0]] = split_rule[1]
polymer = start_polymer


for _ in range(0, 10):
    offset = 1
    for x in range(0, len(polymer)-1):
        part = f"{start_polymer[x]}{start_polymer[x+1]}"
        if part in rules:
            polymer = f"{polymer[:x+offset]}{rules[part]}{polymer[x+offset:]}"
            offset += 1
    start_polymer = polymer

occurrences = {}
for char in polymer:
    if char not in occurrences:
        occurrences[char] = 0
    occurrences[char] += 1

occurrences_vals = occurrences.values()
print(max(occurrences_vals) - min(occurrences_vals))
