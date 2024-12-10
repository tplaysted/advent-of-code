input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines = lines[0:len(lines)-1]
lines = [[int(x) for x in line] for line in lines]

height = len(lines)
width = len(lines[0])

def get_num_reachable(i, j):  # recursive search for a given trailhead
    cur_height = lines[i][j]

    if cur_height == 9 and (i, j):
        return 1

    reachable = 0
    adj = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]

    for next in adj:
        if next[0] < 0 or next[0] >= width:
            continue

        if next[1] < 0 or next[1] >= height:
            continue

        if lines[next[0]][next[1]] == cur_height + 1:
            reachable += get_num_reachable(next[0], next[1])

    return reachable

total = 0

for i in range(height):
    for j in range(width):
        if lines[i][j] == 0:
            total += get_num_reachable(i, j)

print(total)
