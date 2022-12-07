with open('d1-input.txt', 'r') as file:
    lines = file.readlines()

numbers = [int(line.strip()) for line in lines]
num = 0
prev = None
for number in numbers:
    if prev is not None and number > prev:
        num += 1
    prev = number

print(num)
