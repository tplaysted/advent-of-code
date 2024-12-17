input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

exp = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}

lines = input.split('\n')
warehouse = [[exp[x] for x in line] for line in lines[0:len(lines[0])]]
warehouse = [[x for x in ''.join(line)] for line in warehouse]
warehouse = [[x for x in line] for line in warehouse]  # gotta be a better way to do that
moves = [x for line in lines[len(lines[0]):-1] for x in line]

bot = [0, 0]

for i, line in enumerate(warehouse):
    for j, x in enumerate(line):
        if x == '@':
            bot = [i, j]  # find the robot

dirs = {'^': (-1, 0), '<': (0, -1), '>': (0, 1), 'v': (1, 0)}

def group(root, dir, preds):  # recursively find all the things to get pushed
    x, y = root[0], root[1]
    dx, dy = dirs[dir][0], dirs[dir][1]
    obj = warehouse[x][y]

    if (x, y) in preds:
        return preds

    if obj == '@':
        preds[(x, y)] = obj
        return group((x+dx, y+dy), dir, preds)

    if obj == ']':
        preds[(x, y)] = obj
        preds = group((x, y-1), dir, preds)
        return group((x+dx, y+dy), dir, preds)

    if obj == '[':
        preds[(x, y)] = obj
        preds = group((x, y+1), dir, preds)
        return group((x+dx, y+dy), dir, preds)

    return preds

def push(robot, dir):
    clump = group(robot, dir, {})
    dx, dy = dirs[dir][0], dirs[dir][1]

    if not all([warehouse[x+dx][y+dy] != '#' for x, y in clump]):
        return robot  # path is not clear

    for x, y in clump:
        warehouse[x][y] = '.'

    for x, y in clump:
        warehouse[x+dx][y+dy] = clump[(x, y)]

    return [robot[0]+dx, robot[1]+dy]

for move in moves:
    bot = push(bot, move)

h, w = len(warehouse), len(warehouse[0])
total = sum([100 * i + j for j in range(w) for i in range(h) if warehouse[i][j] == '['])

print('\n'.join([''.join(x) for x in warehouse]))
print(total)
