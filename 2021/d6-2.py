with open("d6-input.txt", "r") as f:
    content = f.read()

start_fishes = [int(x) for x in content.strip().split(",")]

fishes = []
fishes.append(0)
for n in range(1, 10):
    fishes.append(len([x for x in start_fishes if x == n-1]))

day = 0
while day < 256:
    for n in range(1, 10):
        fishes[n-1] += fishes[n]
        fishes[n] = 0
    fishes[7] += fishes[0]
    fishes[9] += fishes[0]
    fishes[0] = 0
    day += 1

print(sum(fishes))
