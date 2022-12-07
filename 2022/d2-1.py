with open("d2-input.txt") as f:
    data = f.read().splitlines()

Rock = 1
Paper = 2
Scissors = 3

mapping = {
    "A": Rock,
    "B": Paper,
    "C": Scissors,
    "X": Rock,
    "Y": Paper,
    "Z": Scissors,
}

def wins(you, other):
    if you == other:
        return None
    if you == Rock and other == Scissors:
        return True
    if you == Paper and other == Rock:
        return True
    if you == Scissors and other == Paper:
        return True
    return False


score = 0
for line in data:
    other, you = [mapping[i] for i in line.split(" ")]
    score += you
    res = wins(you, other)
    if res is None:
        score += 3
    if res is True:
        score += 6
print(score)
