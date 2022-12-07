from collections import Counter

with open('d5-input.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def at_least_twice(string):
    for i, letter in enumerate(list(string)):
        if i >= len(string)-1:
            break
        pair = f"{letter}{string[i+1]}"
        occurrences = 0
        j = 0
        while j < len(string)-1:
            comp_pair = f"{string[j]}{string[j+1]}"
            if comp_pair == pair:
                occurrences += 1
                j += 1
            j += 1
        if occurrences == 2:
            return True

    return False

def letters_with_one_in_middle(string):
    for i, letter in enumerate(list(string)):
        if i < len(string)-2 and letter == string[i+2]:
            return True
    return False
nice = 0
for line in lines:
    if at_least_twice(line) and letters_with_one_in_middle(line):
        nice += 1
print(nice)
