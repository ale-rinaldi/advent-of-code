with open("d15-input.txt") as f:
    data = f.read().splitlines()

sensors = {}


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for line in data:
    space_splitted = line.split(" ")
    sensor_x_raw = space_splitted[2]
    sensor_y_raw = space_splitted[3]
    sensor_x = int(sensor_x_raw.strip("x=,"))
    sensor_y = int(sensor_y_raw.strip("y=:"))
    beacon_x_raw = space_splitted[8]
    beacon_y_raw = space_splitted[9]
    beacon_x = int(beacon_x_raw.strip("x=,"))
    beacon_y = int(beacon_y_raw.strip("y=:"))
    sensors[(sensor_x, sensor_y)] = manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y))

LIMIT = 4000000


def get_external_points(sensor, distance, row) -> set:
    y_distance = abs(sensor[1] - row)
    x_distance = distance - y_distance
    result = set()
    left = sensor[0] - x_distance - 1
    right = sensor[0] + x_distance + 1
    if left >= 0 and left <= LIMIT:
        result.add(left)
    if right >= 0 and right <= LIMIT:
        result.add(right)
    return result


def is_inside_range(sensor, distance, row, target) -> bool:
    y_distance = abs(sensor[1] - row)
    x_distance = distance - y_distance
    left = sensor[0] - x_distance
    right = sensor[0] + x_distance
    return target >= left and target <= right


found_x = None
found_y = None

for y in range(0, LIMIT + 1):
    if y % 1000 == 0:
        print(f"Progress: {'{:10.2f}'.format((y / LIMIT) * 100)} %")
    possible_points = set()
    for sensor, distance in sensors.items():
        possible_points.update(get_external_points(sensor, distance, y))
    for point in list(possible_points):
        for sensor, distance in sensors.items():
            if is_inside_range(sensor, distance, y, point):
                possible_points.remove(point)
                break
    if len(possible_points) > 0:
        found_y = y
        found_x = possible_points.pop()
        break

if found_x is not None and found_y is not None:
    print(found_x * 4000000 + found_y)
