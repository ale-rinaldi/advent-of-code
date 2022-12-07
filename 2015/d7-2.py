import numpy, sys

with open('d7-input.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def parse_line(line):
    splitted = line.split(' ')
    if splitted[1] == "AND":
        return {
            "op": "and",
            "one": splitted[0],
            "two": splitted[2],
            "dest": splitted[4] 
        }
    elif splitted[1] == "OR":
        return {
            "op": "or",
            "one": splitted[0],
            "two": splitted[2],
            "dest": splitted[4] 
        }
    elif splitted[1] == "LSHIFT":
        return {
            "op": "lshift",
            "what": splitted[0],
            "shift": int(splitted[2]),
            "dest": splitted[4]
        }
    elif splitted[1] == "RSHIFT":
        return {
            "op": "rshift",
            "what": splitted[0],
            "shift": int(splitted[2]),
            "dest": splitted[4]
        }
    elif splitted[0] == "NOT":
        return {
            "op": "not",
            "what": splitted[1],
            "dest": splitted[3]
        }
    else:
        return {
            "op": "assign",
            "val": splitted[0],
            "dest": splitted[2]
        }

wires = {}
for line in lines:
    op = parse_line(line)
    wires[op["dest"]] = op

vals_cache = {}

def get_value(wire):
    try:
        return int(wire)
    except:
        if wire in vals_cache:
            return vals_cache[wire]
        op = wires[wire]
        if op["op"] == "and":
            val = get_value(op["one"]) & get_value(op["two"])
            vals_cache[wire] = val
            return val
        elif op["op"] == "or":
            val = get_value(op["one"]) | get_value(op["two"])
            vals_cache[wire] = val
            return val
        elif op["op"] == "lshift":
            val = get_value(op["what"]) << op["shift"]
            vals_cache[wire] = val
            return val
        elif op["op"] == "rshift":
            val = get_value(op["what"]) >> op["shift"]
            vals_cache[wire] = val
            return val
        elif op["op"] == "not":
            val = ~get_value(op["what"])
            vals_cache[wire] = val
            return val
        elif op["op"] == "assign":
            val = get_value(op["val"])
            vals_cache[wire] = val
            return val
        raise ValueError(op)

val = get_value("a")
wires["b"] = {
    "op": "assign",
    "val": f"{val}",
    "dest": "b"
}
vals_cache = {}
print(numpy.uint16(get_value("a")))
