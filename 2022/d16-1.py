import itertools

from astar import AStar

with open("d16-input.txt") as f:
    data = f.read().splitlines()

TIME_LIMIT = 30

valves = set()
valve_flow_rate = {}
valve_neighbors = {}
point_max_score = {}
valve_distances = {}

for line in data:
    valve_name = line.split(" ")[1]
    i_valve_flow_rate = int(line.split(" ")[4].split("=")[1].strip(";"))
    i_valve_neighbors = [n.strip(", ") for n in line.split(" ")[9:]]
    valves.add(valve_name)
    valve_flow_rate[valve_name] = i_valve_flow_rate
    valve_neighbors[valve_name] = i_valve_neighbors


def get_valves_distance(valve1, valve2):
    class MyAStar(AStar):
        def neighbors(self, node):
            return valve_neighbors[node]

        def distance_between(self, n1, n2) -> float:
            return 1

        def heuristic_cost_estimate(self, current, goal) -> float:
            # Returning a random number just eliminates any heuristic, and makes this a Dijkstra
            return 100

    myastar = MyAStar()
    solution = myastar.astar(valve1, valve2)
    return len(list(solution)) - 1


for valve in valves:
    for other_valve in valves:
        if valve == other_valve:
            continue
        if valve not in valve_distances:
            valve_distances[valve] = {}
        valve_distances[valve][other_valve] = get_valves_distance(valve, other_valve)

valves_worth_opening = [k for k, v in valve_flow_rate.items() if v > 0]


class ScoreCalculator:
    time: int
    score: int
    open_valves: set
    elements: list
    current_point: str

    def __init__(self, elements):
        self.time = 0
        self.score = 0
        self.open_valves = set()
        self.elements = elements
        self.current_point = "AA"

    def _time_tick(self):
        self.time += 1
        for valve in self.open_valves:
            self.score += valve_flow_rate[valve]

    def _move(self, destination_point):
        distance = valve_distances[self.current_point][destination_point]
        for _ in range(distance):
            self._time_tick()
            if self.time == 30:
                return False
        self.current_point = destination_point
        return True

    def _open_valve(self):
        self._time_tick()
        self.open_valves.add(self.current_point)

    def calculate_score(self):
        for element in self.elements:
            if not self._move(element) or self.time == 30:
                return self.score
            self._open_valve()
            if self.time == 30:
                return self.score
        while self.time < 30:
            self._time_tick()
        return self.score


scores = []
permutations = itertools.permutations(valves_worth_opening)

for permutation in permutations:
    scores.append(ScoreCalculator(permutation).calculate_score())

print(max(scores))
