input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
warehouse = [[x for x in line] for line in lines[0:len(lines[0])]]
moves = [x for line in lines[len(lines[0]):-1] for x in line]

bot = [0, 0]

for i, line in enumerate(warehouse):
    for j, x in enumerate(line):
        if x == '@':
            bot = [i, j]  # find the robot

dirs = {'^': (-1, 0), '<': (0, -1), '>': (0, 1), 'v': (1, 0)}

def push(robot, d):  # push boxes if you can
    x, y = robot[0], robot[1]
    dx, dy = dirs[d][0], dirs[d][1]
    while True:
        x += dx
        y += dy
        next = warehouse[x][y]

        if next == '.':
            while x != robot[0] or y != robot[1]:
                warehouse[x][y] = warehouse[x-dx][y-dy]
                x -= dx
                y -= dy

            warehouse[robot[0]][robot[1]] = '.'
            return [robot[0] + dx, robot[1] + dy]

        if next == '#':
            return robot

for move in moves:
    bot = push(bot, move)

n = len(warehouse)
total = sum([100 * i + j for j in range(n) for i in range(n) if warehouse[i][j] == 'O'])

print('\n'.join([''.join(x) for x in warehouse]))
print(total)
