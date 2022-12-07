with open("d4-input.txt") as f:
    data = f.read().splitlines()

count = 0
for line in data:
    pair1s, pair2s = [p.split("-") for p in line.split(",")]
    pair1 = set(range(int(pair1s[0]), int(pair1s[1]) + 1))
    pair2 = set(range(int(pair2s[0]), int(pair2s[1]) + 1))
    if len(list(pair1 - pair2)) == 0 or len(list(pair2-pair1)) == 0:
        count += 1

print(count)
