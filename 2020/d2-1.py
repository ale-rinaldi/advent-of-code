from collections import Counter

with open("d2-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

valid = 0
for line in lines:
    policy_arr = line.split(": ")
    password = policy_arr[1]
    policy_arr = policy_arr[0].split(" ")
    character = policy_arr[1]
    policy_arr = policy_arr[0].split("-")
    min = int(policy_arr[0])
    max = int(policy_arr[1])
    counter = Counter(password)
    if counter[character] >= min and counter[character] <= max:
        valid += 1

print(valid)
