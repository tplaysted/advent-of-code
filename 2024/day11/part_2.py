input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

line = input.split('\n')[0]
stones = [int(x) for x in line.split(' ')]

lookup = {}  # a hash table to store previously computed values

def expand(stone: int, depth):  # still exponential but totally fine
    if depth == 0:
        return 1

    if (stone, depth) in lookup:
        return lookup[(stone, depth)]

    size = 0

    if stone == 0:
        size = expand(1, depth - 1)

    if len(str(stone)) % 2  == 0:
        n = len(str(stone))
        left = int(str(stone)[0:n // 2])  # kill leading zeroes
        right = int(str(stone)[n // 2: n])

        size = expand(left, depth - 1) + expand(right, depth - 1)

    if size == 0:
        size = expand((stone * 2024), depth - 1)

    lookup[(stone, depth)] = size  # keep that in your pocket for later

    return size

total = sum([expand(x, 75) for x in stones])

print(total)
