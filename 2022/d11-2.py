import math
from typing import List, Dict, Optional

with open("d11-input.txt") as f:
    data = f.read().strip()

lcm = 0

class Object:
    worry_level: int

    def __init__(self, worry_level: int):
        self.worry_level = worry_level

    def __repr__(self):
        return str(self.worry_level)

class Monkey:
    number: int
    objs: List[Object]
    operation_sign: str
    operation_number: Optional[int] = None
    divisible_test: int
    if_true_dst: "Monkey"
    if_false_dst: "Monkey"

    def append_object(self, obj: Object):
        self.objs.append(obj)

    def _inspect_object(self, obj: Object):
        op_num = self.operation_number
        if op_num is None:
            op_num = obj.worry_level
        if self.operation_sign == "+":
            obj.worry_level += op_num
        elif self.operation_sign == "*":
            obj.worry_level *= op_num
        else:
            raise Exception("invalid operation sign")
        obj.worry_level %= lcm
        if obj.worry_level % self.divisible_test == 0:
            dst = self.if_true_dst
        else:
            dst = self.if_false_dst
        dst.append_object(obj)

    def run_inspect(self):
        for obj in self.objs:
            self._inspect_object(obj)
            if self.number not in monkey_inspected:
                monkey_inspected[self.number] = 0
            monkey_inspected[self.number] += 1
        self.objs = []

    def __repr__(self):
        return f"<Monkey number={self.number} objs={[o.worry_level for o in self.objs]}>"


monkeys_str = data.split("\n\n")
monkeys: Dict[int, Monkey] = {}
monkey_inspected: Dict[int, int] = {}

for monkey_str in monkeys_str:
    monkey_split = monkey_str.splitlines()
    monkey_number = int(monkey_split[0].strip().split(" ")[1].strip(":"))
    if monkey_number in monkeys:
        monkey = monkeys[monkey_number]
    else:
        monkey = Monkey()
    monkey.number = monkey_number
    monkey.objs = [Object(int(o.strip())) for o in monkey_split[1].split(":")[1].split(",")]
    monkey.operation_sign = monkey_split[2].strip().split(" ")[4]
    operation_number_str = monkey_split[2].strip().split(" ")[5]
    if operation_number_str != "old":
        monkey.operation_number = int(operation_number_str)
    monkey.divisible_test = int(monkey_split[3].strip().split(" ")[3])
    if_true_dst_num = int(monkey_split[4].strip().split(" ")[5])
    if if_true_dst_num not in monkeys:
        monkeys[if_true_dst_num] = Monkey()
    monkey.if_true_dst = monkeys[if_true_dst_num]
    if_false_dst_num = int(monkey_split[5].strip().split(" ")[5])
    if if_false_dst_num not in monkeys:
        monkeys[if_false_dst_num] = Monkey()
    monkey.if_false_dst = monkeys[if_false_dst_num]
    monkeys[monkey_number] = monkey


def get_sorted_monkeys():
    monkeys_list = list(monkeys.values())
    monkeys_list.sort(key=lambda m: m.number)
    return monkeys_list


lcm = math.lcm(*[m.divisible_test for m in monkeys.values()])

rounds = 10000
for round in range(rounds):
    for monkey in get_sorted_monkeys():
        monkey.run_inspect()

insp_list = list(monkey_inspected.values())
insp_list.sort(reverse=True)
print(insp_list[0] * insp_list[1])
