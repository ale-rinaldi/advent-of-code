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
    pos1 = int(policy_arr[0])
    pos2 = int(policy_arr[1])
    match1 = password[pos1-1] == character
    match2 = password[pos2-1] == character
    if (match1 and not match2) or (match2 and not match1):
        valid += 1

print(valid)
