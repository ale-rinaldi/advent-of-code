with open("d15-input.txt") as f:
    data = f.read().splitlines()

sensors = {}
min_x = 0
max_x = 0
min_y = 0
max_y = 0

TARGET_COLUMN = 2000000


def update_maxes(x, y):
    global min_x, max_x, min_y, max_y
    if min_x > x:
        min_x = x
    if max_x < x:
        max_x = x
    if min_y > y:
        min_y = y
    if max_y < y:
        max_y = y


for line in data:
    space_splitted = line.split(" ")
    sensor_x_raw = space_splitted[2]
    sensor_y_raw = space_splitted[3]
    sensor_x = int(sensor_x_raw.strip("x=,"))
    sensor_y = int(sensor_y_raw.strip("y=:"))
    update_maxes(sensor_x, sensor_y)
    beacon_x_raw = space_splitted[8]
    beacon_y_raw = space_splitted[9]
    beacon_x = int(beacon_x_raw.strip("x=,"))
    beacon_y = int(beacon_y_raw.strip("y=:"))
    update_maxes(beacon_x, beacon_y)
    sensors[(sensor_x, sensor_y)] = (beacon_x, beacon_y)

sensors_set = set(sensors.keys())
beacons_set = set(sensors.values())


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


total_sensors = len(sensors.keys())
safe_spots = set()
for sensor, beacon in sensors.items():
    max_distance = manhattan_distance(sensor, beacon)
    distance = abs(TARGET_COLUMN - sensor[1])
    if distance > max_distance:
        continue
    x_distance = max_distance - distance
    lower_x = sensor[0] - x_distance
    upper_x = sensor[0] + x_distance
    x = lower_x
    while x <= upper_x:
        if (x, TARGET_COLUMN) not in beacons_set:
            safe_spots.add((x, TARGET_COLUMN))
        x += 1


def safe_spots_at_column(col):
    return len([p for p in safe_spots if p[1] == col])


print(safe_spots_at_column(TARGET_COLUMN))
