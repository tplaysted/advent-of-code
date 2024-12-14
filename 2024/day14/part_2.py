import re
import math

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
safety = (math.inf, 0)

for i in range(width * height):
    for r in robots:
        r[0] = (r[0] + r[2]) % width
        r[1] = (r[1] + r[3]) % height

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

    if total < safety[0]:  # if they're clumped together the 'safety' score will be low
        safety = (total, i)
        print(total)
        grid = [['.' for _ in range(width)] for _ in range(height)]

        for r in robots:
            grid[r[1]][r[0]] = '#'

        print('\n'.join([''.join(line) for line in grid]))  # for manual checking

print(safety[0], safety[1])
