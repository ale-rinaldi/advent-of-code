with open("d10-input.txt") as f:
    data = f.read().splitlines()

register = 1
cycle = 1

strengths = []


def cycle_callback():
    if cycle == 20 or (cycle - 20) % 40 == 0:
        strengths.append(cycle * register)


for instr in data:
    s_instr = instr.split(" ")
    if s_instr[0] == "noop":
        cycle_callback()
        cycle += 1
        continue

    elif s_instr[0] == "addx":
        cycle_callback()
        cycle += 1

        cycle_callback()
        register += int(s_instr[1])
        cycle += 1

print(sum(strengths))
