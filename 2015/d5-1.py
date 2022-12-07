with open('d5-input.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def has_three_vowels(string):
    return len([x for x in list(string) if x in ['a', 'e', 'i', 'o', 'u']]) > 2

def letters_in_a_row(string):
    for i, letter in enumerate(list(string)):
        if i < len(string)-1 and letter == string[i+1]:
            return True
    return False

def no_forbidden(string):
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        return False
    return True

nice = 0
for line in lines:
    if has_three_vowels(line) and letters_in_a_row(line) and no_forbidden(line):
        nice += 1
print(nice)
