with open("d12-input.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

caves = {}
for line in lines:
    splitted = line.split("-")
    cave_a = splitted[0]
    cave_b = splitted[1]
    if cave_a not in caves:
        caves[cave_a] = {
            "conn": [cave_b],
            "mult": cave_a.upper() == cave_a
        }
    else:
        caves[cave_a]["conn"].append(cave_b)
    if cave_b not in caves:
        caves[cave_b] = {
            "conn": [cave_a],
            "mult": cave_b.upper() == cave_b
        }
    else:
        caves[cave_b]["conn"].append(cave_a)

paths = []
def find_paths(cave_name, path = [], visited = []):
    visited = list(visited)
    path = list(path)
    path.append(cave_name)
    if cave_name == "end":
        paths.append(path)
        return
    cave = caves[cave_name]
    if not cave["mult"]:
        visited.append(cave_name)
    for conn in cave["conn"]:
        if conn not in visited:
            find_paths(conn, path, visited)

find_paths("start")

print(len(paths))
