with open('d2-input.txt', 'r') as file:
    lines = file.readlines()

horizontal = 0
depth = 0
for line in lines:
    list = line.split(" ")
    command = list[0]
    num = int(list[1])
    if command == "forward":
        horizontal += num
    elif command == "down":
        depth += num
    elif command == "up":
        depth -= num

print(horizontal*depth)
