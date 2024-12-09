input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines.pop() # last line blank

n = len(lines)

centers = [(i, j) for i in range(1,n-1) for j in range(1,n-1)]
centers = list(filter(lambda x: lines[x[0]][x[1]] == 'A', centers))

def is_x_mas(i, j):
    tl = lines[i-1][j-1]
    br = lines[i+1][j+1]
    tr = lines[i+1][j-1]
    bl = lines[i-1][j+1]

    if not ((tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')):
        return False

    if not ((tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M')):
        return False

    return True

centers = list(filter(lambda x: is_x_mas(x[0], x[1]), centers))

print(len(centers))
