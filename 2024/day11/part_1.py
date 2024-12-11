input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

line = input.split('\n')[0]
stones = [int(x) for x in line.split(' ')]

def expand(stone: int, depth):  # exponentially bad but obvious
    if depth == 0:
        return 1

    if stone == 0:
        return expand(1, depth - 1)

    if len(str(stone)) % 2  == 0:
        n = len(str(stone))
        left = int(str(stone)[0:n // 2])  # kill leading zeroes
        right = int(str(stone)[n // 2: n])

        return expand(left, depth - 1) + expand(right, depth - 1)

    return expand((stone * 2024), depth - 1)

total = sum([expand(x, 25) for x in stones])

print(total)
