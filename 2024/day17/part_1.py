import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

a = int(re.findall('Register A: (\\d+)', input)[0])
b = int(re.findall('Register B: (\\d+)', input)[0])
c = int(re.findall('Register C: (\\d+)', input)[0])

reg = [a, b, c]
output = []

pgrm = [int(x) for x in re.findall('Program: ([\\d+,]+)\n', input)[0].split(',')]
ptr = [0]  # ints don't really play nice in global scope

def combo(op):
    map = {0: 0, 1: 1, 2: 2, 3: 3, 4: reg[0], 5: reg[1], 6: reg[2]}
    return map[op]

def adv(op):
    reg[0] = reg[0] // 2 ** combo(op)
    ptr[0] += 2

def bxl(op):
    reg[1] = reg[1] ^ op
    ptr[0] += 2

def bst(op):
    reg[1] = combo(op) % 8
    ptr[0] += 2

def jnz(op):
    if reg[0] != 0:
        ptr[0] = op
    else:
        ptr[0] += 2

def bxc(op):
    reg[1] = reg[1] ^ reg[2]
    ptr[0] += 2

def out(op):
    output.append(combo(op) % 8)
    ptr[0] += 2

def bdv(op):
    reg[1] = reg[0] // 2 ** combo(op)
    ptr[0] += 2

def cdv(op):
    reg[2] = reg[0] // 2 ** combo(op)
    ptr[0] += 2

opcodes = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

while ptr[0] < len(pgrm) - 1:
    cmd = opcodes[pgrm[ptr[0]]]
    op = pgrm[ptr[0] + 1]
    cmd(op)

print(','.join(str(x) for x in output))
