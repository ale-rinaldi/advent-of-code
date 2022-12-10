with open("d10-input.txt") as f:
    data = f.read().splitlines()

register = 1
cycle = 1

monitor_pixels = set()


def calculate_point(ref):
    x = (ref - 1) % 40
    y = (ref - 1) // 40
    while y > 5:
        y -= 5
    return x, y


def cycle_callback():
    x = (cycle - 1) % 40
    y = (cycle - 1) // 40
    while y > 5:
        y -= 5
    point = calculate_point(cycle)

    sprike = [(register-1, y), (register, y), (register + 1, y)]
    if point in sprike:
        monitor_pixels.add(point)


def render_matrix():
    max_x = max([p[0] for p in monitor_pixels])
    max_y = max([p[1] for p in monitor_pixels])
    for y in range(0, max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if (x, y) in monitor_pixels:
                line += "#"
            else:
                line += "."
        print(line)


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

render_matrix()
