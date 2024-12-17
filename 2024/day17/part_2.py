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

def run():
    ptr[0] = 0
    while ptr[0] < len(pgrm) - 1:
        cmd = opcodes[pgrm[ptr[0]]]
        op = pgrm[ptr[0] + 1]
        cmd(op)

# the program outputs exactly once per iteration, so we can backtrack
# the A value is shifted right 3 bits every iteration

def ans(sol, depth):  # recursive search
    if depth > len(pgrm):
        return sol

    target = pgrm[-depth:]

    for i in range(8):
        global output
        output = []
        global reg
        reg = [(sol << 3) + i, 0, 0]
        run()

        if output == target:
            pot = ans((sol << 3) + i, depth + 1)
            if pot is not None:
                return pot


print(ans(0, 1))
