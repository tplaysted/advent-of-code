import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')

outputs = {}
parents = {}
ops = {'XOR': lambda a,b: a^b, 'AND': lambda a,b: a&b, 'OR': lambda a,b: a|b}

for line in lines:
    if len(line) == 6:
        outputs[line[0:3]] = int(line[5])

    if len(line) > 6:
        p1 = line[0:3]
        p2 = line[-10:-7]
        name = line[-3:]
        op = re.findall('(XOR|AND|OR)', line)[0]

        parents[name] = (p1, p2, op)

def get_value(name):
    if name in outputs:
        return outputs[name]

    p1, p2, op = parents[name]
    outputs[name] = ops[op](get_value(p1), get_value(p2))
    return outputs[name]

[get_value(x) for x in parents]
bin = [outputs[x] for x in sorted(list(filter(lambda x: x[0] == 'z', outputs)))]

total = 0

for b in reversed(bin):
    total = (total << 1) | b

print(total)
