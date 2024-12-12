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

    perim = 0
    adj = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]

    for next in adj:  # find perimeter contribution of plot
        if next[0] < 0 or next[0] >= height:
            perim += 1  # never touches top and bottom
            continue

        if next[1] < 0 or next[1] >= width:
            perim += 1
            continue

        if lines[next[0]][next[1]] != label:
            perim += 1

    searched[(i, j)] = perim  # mark as seen and move on

    for next in adj:  # keep exploring blob
        if next[0] < 0 or next[0] >= height:
            continue

        if next[1] < 0 or next[1] >= width:
            continue

        crawl(next[0], next[1], label, searched)

    return searched

map = [['.' for _ in line] for line in lines]  # will keep track of counted blobs
total = 0

for i in range(height):  # find the answer
    for j in range(width):
        if map[i][j] == '.':
            blob = crawl(i, j, lines[i][j], {})
            perim = 0

            for (c, p) in blob.items():
                perim += p
                map[c[0]][c[1]] = 'X'

            total += len(blob) * perim

print(total)
