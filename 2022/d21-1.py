from typing import Optional

with open("d21-input.txt") as f:
    data = f.read().splitlines()


class Monkey:
    name: str
    raw_value: Optional[int] = None
    monkey1: Optional[str] = None
    monkey2: Optional[str] = None
    operation: Optional[str] = None

    def __init__(self, line):
        pieces = [p.strip() for p in line.split(":")]
        self.name = pieces[0]
        try:
            self.raw_value = int(pieces[1])
        except ValueError:
            self.raw_value = None
            op_pieces = pieces[1].split(" ")
            self.monkey1 = op_pieces[0]
            self.operation = op_pieces[1]
            self.monkey2 = op_pieces[2]

class Monkeys:
    monkeys: dict
    def __init__(self, data):
        self.monkeys = {}
        for line in data:
            monkey = Monkey(line)
            self.monkeys[monkey.name] = monkey

    def get_monkey_value(self, name):
        monkey = self.monkeys[name]
        if monkey.raw_value is not None:
            return monkey.raw_value
        monkey1_value = self.get_monkey_value(monkey.monkey1)
        monkey2_value = self.get_monkey_value(monkey.monkey2)
        if monkey.operation == "+":
            result = monkey1_value + monkey2_value
        elif monkey.operation == "-":
            result = monkey1_value - monkey2_value
        elif monkey.operation == "*":
            result = monkey1_value * monkey2_value
        elif monkey.operation == "/":
            result = monkey1_value // monkey2_value
        else:
            raise ValueError(f"Invalid operation {monkey.operation}")
        monkey.raw_value = result
        return result


monkeys = Monkeys(data)
print(monkeys.get_monkey_value("root"))
