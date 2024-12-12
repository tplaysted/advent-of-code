input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines = [[x for x in line] for line in lines[:-1]]  # list is easier to work with

height = len(lines)
width = len(lines[0])

def crawl(i, j, label, searched):  # crawl a blob given a label. return dict of {coords: perim}
    if (i, j) in searched:
        return searched

    if lines[i][j] != label:
        return searched

    adj = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
    searched[(i, j)] = 0  # mark as seen and move on

    for next in adj:  # keep exploring blob
        if next[0] < 0 or next[0] >= height:
            continue

        if next[1] < 0 or next[1] >= width:
            continue

        crawl(next[0], next[1], label, searched)

    return searched

def corners(blob):  # there are as many straight sides as corners!
    padded = [['.' for _ in range(width + 2)] for _ in range(height + 2)]
    corners = 0

    for c in blob:
        padded[c[0] + 1][c[1] + 1] = 'X'

    for c in blob:
        nb = [[padded[i][j] for j in range(c[1], c[1] + 3)] for i in range(c[0], c[0] + 3)]

        if (nb[0][1] == '.' and nb[1][0] == '.') or (nb[0][1] == 'X' and nb[1][0] == 'X' and nb[0][0] == '.'):
            corners += 1

        if (nb[0][1] == '.' and nb[1][2] == '.') or (nb[0][1] == 'X' and nb[1][2] == 'X' and nb[0][2] == '.'):
            corners += 1

        if (nb[2][1] == '.' and nb[1][0] == '.') or (nb[2][1] == 'X' and nb[1][0] == 'X' and nb[2][0] == '.'):
            corners += 1

        if (nb[2][1] == '.' and nb[1][2] == '.') or (nb[2][1] == 'X' and nb[1][2] == 'X' and nb[2][2] == '.'):
            corners += 1

    return corners

map = [['.' for _ in line] for line in lines]  # will keep track of counted blobs
total = 0

for i in range(height):  # find the answer
    for j in range(width):
        if map[i][j] == '.':
            blob = crawl(i, j, lines[i][j], {})

            for (c, p) in blob.items():
                map[c[0]][c[1]] = 'X'

            total += len(blob) * corners(blob)

print(total)
