import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
machines = []

for i in range(len(lines) // 4):
    a = (int(re.findall('X\\+(\\d+)', lines[4 * i])[0]), int(re.findall('Y\\+(\\d+)', lines[4 * i])[0]))
    b = (int(re.findall('X\\+(\\d+)', lines[4 * i + 1])[0]), int(re.findall('Y\\+(\\d+)', lines[4 * i + 1])[0]))
    prize = (int(re.findall('X=(\\d+)', lines[4 * i + 2])[0]), int(re.findall('Y=(\\d+)', lines[4 * i + 2])[0]))
    machines.append((a, b, prize))

def cost(a, b, prize):
    det = a[0] * b[1] - a[1] * b[0]  # det!=0 assuming all are linearly independent; i checked
    x = b[1] * prize[0] - b[0] * prize[1]
    y = a[0] * prize[1] - a[1] * prize[0]

    if x % det == 0 and y % det == 0:
        return 3 * (x // det) + y // det

    return 0

print(sum([cost(m[0], m[1], m[2]) for m in machines]))
