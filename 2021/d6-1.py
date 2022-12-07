with open("d6-input.txt", "r") as f:
    content = f.read()

fishes = [int(x) for x in content.strip().split(",")]

day = 0
while day < 80:
    i = 0
    new_fishes = []
    while i < len(fishes):
        fishes[i] -= 1
        if fishes[i] < 0:
            new_fishes.append(8)
            fishes[i] = 6
        i += 1
    fishes += new_fishes
    day += 1

print(len(fishes))
