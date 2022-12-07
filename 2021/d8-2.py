with open("d8-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def resolve(parts):
    one = [list(p) for p in parts if len(p) == 2][0]
    one.sort()
    four = [list(p) for p in parts if len(p) == 4][0]
    four.sort()
    seven = [list(p) for p in parts if len(p) == 3][0]
    seven.sort()
    eight = [list(p) for p in parts if len(p) == 7][0]
    eight.sort()
    
    zeros = [list(p) for p in parts if len(p) == 6 and len(set(seven).intersection(p)) == 3 and len(set(four).intersection(p)) == 3]
    if len(zeros) != 1:
        raise ValueError(f"{len(zeros)} zeros found")
    zero = zeros[0]
    zero.sort()
    
    twos = [list(p) for p in parts if len(p) == 5 and len(set(seven).intersection(p)) == 2 and len(set(four).intersection(p)) == 2]
    if len(twos) != 1:
        raise ValueError(f"{len(twos)} twos found")
    two = twos[0]
    two.sort()
    
    threes = [list(p) for p in parts if len(p) == 5 and len(set(seven).intersection(p)) == 3 and len(set(four).intersection(p)) == 3]
    if len(threes) != 1:
        raise ValueError(f"{len(threes)} threes found")
    three = threes[0]
    three.sort()
    
    fives = [list(p) for p in parts if len(p) == 5 and len(set(seven).intersection(p)) == 2 and len(set(four).intersection(p)) == 3]
    if len(fives) != 1:
        raise ValueError(f"{len(fives)} fives found")
    five = fives[0]
    five.sort()

    sixes = [list(p) for p in parts if len(p) == 6 and len(set(seven).intersection(p)) == 2 and len(set(four).intersection(p)) == 3]
    if len(sixes) != 1:
        raise ValueError(f"{len(sixes)} sixes found")
    six = sixes[0]
    six.sort()

    nines = [list(p) for p in parts if len(p) == 6 and len(set(seven).intersection(p)) == 3 and len(set(four).intersection(p)) == 4]
    if len(nines) != 1:
        raise ValueError(f"{len(nines)} nines found")
    nine = nines[0]
    nine.sort()

    return {
        "".join(zero): 0,
        "".join(one): 1,
        "".join(two): 2,
        "".join(three): 3,
        "".join(four): 4,
        "".join(five): 5,
        "".join(six): 6,
        "".join(seven): 7,
        "".join(eight): 8,
        "".join(nine): 9,
    }

sum = 0
for line in lines:
    parts = line.split(" | ")
    digits = resolve(parts[0].split(" "))
    outputs = parts[1].split(" ")
    res_list = []
    for digit in outputs:
        digit_list = list(digit)
        digit_list.sort()
        res_list.append(str(digits["".join(digit_list)]))
    res = int("".join(res_list))
    sum += res

print(sum)
