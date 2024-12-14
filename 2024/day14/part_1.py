import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines.pop()
robots = []

for line in lines:
    x = int(re.findall('p=(-*\\d+)', line)[0])
    y = int(re.findall('p=-*\\d+,(-*\\d+)', line)[0])
    vx = int(re.findall('v=(-*\\d+)', line)[0])
    vy = int(re.findall('v=-*\\d+,(-*\\d+)', line)[0])
    robots.append([x, y, vx, vy])

height = 103
width = 101
time = 100

for r in robots:
    r[0] = (r[0] + r[2] * time) % width
    r[1] = (r[1] + r[3] * time) % height

quads = [0, 0, 0, 0]

for r in robots:
    if r[0] < (width // 2) and r[1] < (height // 2):
        quads[0] += 1

    if r[0] > (width // 2) and r[1] < (height // 2):
        quads[1] += 1

    if r[0] < (width // 2) and r[1] > (height // 2):
        quads[2] += 1

    if r[0] > (width // 2) and r[1] > (height // 2):
        quads[3] += 1

total = 1

for q in quads:
    total *= q

print(total)
