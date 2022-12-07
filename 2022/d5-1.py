import textwrap

with open("d5-input.txt") as f:
    data = f.read()

crates = {}


r_crates, instructions = [g.split("\n") for g in data.split("\n\n")]

del(r_crates[-1])
for crate in r_crates:
    crate = crate.replace("    ", " [ ]")
    crate = textwrap.wrap(crate, 3)
    index = 1
    for s_crate in crate:
        s_crate = s_crate.strip("[] ")
        if not s_crate:
            index += 1
            continue
        if index not in crates:
            crates[index] = []
        crates[index].append(s_crate)
        index += 1

for key in crates.keys():
    crates[key] = crates[key][::-1]

def move(frm, to):

    item = crates[frm].pop()
    crates[to].append(item)

def print_crates():
    max_key = max(crates.keys())
    for idx in range(1, max_key+1):
        print(f"{idx}: {''.join(crates[idx])}")

for instr in instructions:
    l_instr = instr.split(" ")
    qty = int(l_instr[1])
    frm = int(l_instr[3])
    to = int(l_instr[5])
    for _ in range(0, qty):
        move(frm, to)

max_key = max(crates.keys())
res = ""
for key in range(1, max_key+1):
    res += crates[key][-1]

print(res)
