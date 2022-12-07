with open('d1-input.txt', 'r') as file:
    lines = file.readlines()

raw_numbers = [int(line.strip()) for line in lines]

x = 0
sum = 0
numbers = []
for i, number in enumerate(raw_numbers):
    if i == 0:
        numbers.append(number)
    elif i == 1:
        numbers.append(number + raw_numbers[0])
    elif i == len(raw_numbers) - 2:
        numbers.append(number + raw_numbers[len(raw_numbers) - 1])
    elif i == len(raw_numbers) - 1:
        numbers.append(number)
    else:
        numbers.append(number + raw_numbers[i - 1] + raw_numbers[i - 2])

num = 0
prev = None
for number in numbers:
    if prev is not None and number > prev:
        num += 1
    prev = number

print(num)
