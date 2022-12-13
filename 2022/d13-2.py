import functools
from typing import Union, List, Optional
from queue import LifoQueue


class PairList:
    items: List[Union["PairList", int]]

    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def __repr__(self):
        return str(self.items)


class Pair:
    list1: PairList
    list2: PairList

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __repr__(self):
        return f"{self.list1}\n{self.list2}"


def compare(e1: Union[PairList, int], e2: Union[PairList, int]):
    if isinstance(e1, int) and isinstance(e2, int):
        if e1 == e2:
            return None
        return e1 < e2
    if isinstance(e1, int):
        e1 = PairList([e1])
    if isinstance(e2, int):
        e2 = PairList([e2])
    max_length = max(len(e1.items), len(e2.items))
    for i in range(max_length):
        if len(e1.items) <= i:
            return True
        if len(e2.items) <= i:
            return False
        result = compare(e1.items[i], e2.items[i])
        if result is not None:
            return result
    return None


def parse_raw_list(input: str) -> PairList:
    stack = LifoQueue()
    current_list: Optional[PairList] = None
    splitted = [i.strip() for i in input.split(",")]
    for item in splitted:
        ends = 0
        while item.startswith("["):
            if current_list is not None:
                stack.put(current_list)
            current_list = PairList()
            item = item[1:]
        while item.endswith("]"):
            ends += 1
            item = item[:-1]
        if item != "":
            current_list.items.append(int(item))
        while ends > 0:
            if stack.qsize() > 0:
                parent_list = stack.get()
                parent_list.items.append(current_list)
                current_list = parent_list
            ends -= 1
    return current_list


def parse_input() -> List[Pair]:
    result: List[Pair] = []
    with open("d13-input.txt") as f:
        data = f.read().strip()
    raw_pairs = data.split("\n\n")
    for raw_pair in raw_pairs:
        splitted_raw_pair = raw_pair.strip().split("\n")
        list1 = parse_raw_list(splitted_raw_pair[0].strip())
        list2 = parse_raw_list(splitted_raw_pair[1].strip())
        result.append(Pair(list1, list2))
    return result


pairs = parse_input()
packets = []
for p in pairs:
    packets.append({"packet": p.list1, "is_divider": False})
    packets.append({"packet": p.list2, "is_divider": False})

packets.append({"packet": PairList([PairList([2])]), "is_divider": True})
packets.append({"packet": PairList([PairList([6])]), "is_divider": True})


def compare_for_sorted(e1, e2):
    res = compare(e1["packet"], e2["packet"])
    if res is None:
        return 0
    if res:
        return -1
    return 1


srt = sorted(packets, key=functools.cmp_to_key(compare_for_sorted))
i = 1
result = 1

for item in srt:
    if item["is_divider"]:
        result *= i
    i += 1

print(result)
