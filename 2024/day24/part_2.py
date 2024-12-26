import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')

regs = {}  # input registers
parents = {}
children = {}
ops = {'XOR': lambda a,b: a^b, 'AND': lambda a,b: a&b, 'OR': lambda a,b: a|b}

for line in lines:  # define dependencies
    if len(line) == 6:
        regs[line[0:3]] = 0  # zero initialisation

    if len(line) > 6:
        p1 = line[0:3]
        p2 = line[-10:-7]
        name = line[-3:]
        op = re.findall('(XOR|AND|OR)', line)[0]

        children[p1] = name
        children[p2] = name
        parents[name] = (p1, p2, op)

def get_value(name, known):
    if name in regs:
        return regs[name]

    if name in known:
        return known[name]

    p1, p2, op = parents[name]
    known[name] = ops[op](get_value(p1, known), get_value(p2, known))  # update known
    return known[name]

def simulate(x, y):
    inputs = {'x': x, 'y': y}  # numbers we want to add

    for reg in regs:
        regs[reg] = (inputs[reg[0]] >> int(reg[1:3])) % 2

    k = {}
    binary = [get_value(z, k) for z in sorted(list(filter(lambda x: x[0] == 'z', parents)))]
    return sum([(1 << i) * b for i, b in enumerate(binary)])

def print_children(name):
    output = ''
    while name in children:
        output += name + ' -> '
        name = children[name]

    print(output + name)

for reg in regs:
    if reg[0] == 'x':  # just testing each x-reg will let uis inspect z-regs
        num = 1 << int(reg[1:3])
        res = simulate(num, 0)

        if res != num:
            print('\nExpected', num, ', got' , res)
            print_children('x' + f'{int(reg[1:3]):02d}')
