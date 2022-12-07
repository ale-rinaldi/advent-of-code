with open("d2-input.txt") as f:
    data = f.read().splitlines()

Rock = 1
Paper = 2
Scissors = 3

mapping = {
    "A": Rock,
    "B": Paper,
    "C": Scissors,
}

res_mapping = {
    "X": False,
    "Y": None,
    "Z": True,
}


def how_to_win(other):
    if other == Rock:
        return Paper
    if other == Paper:
        return Scissors
    if other == Scissors:
        return Rock


def how_to_lose(other):
    if other == Rock:
        return Scissors
    if other == Paper:
        return Rock
    if other == Scissors:
        return Paper


score = 0
for line in data:
    split_line = line.split(" ")
    other = mapping[split_line[0]]
    res = res_mapping[split_line[1]]
    if res is None:
        you = other
    elif res is True:
        you = how_to_win(other)
    else:
        you = how_to_lose(other)
    score += you
    if res is None:
        score += 3
    if res is True:
        score += 6
print(score)
