from functools import cache  # we will recompute the same designs lots of times

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
blocks = lines[0].split(', ')
designs = lines[2:-2]

@cache
def ways_makeable(design):
    if design == '':
        return 1

    total = 0

    for i in range(1, len(design) + 1):
        part, right = design[0:i], design[i:len(design)]

        if (part in blocks):
            total += ways_makeable(right)

    return total

print(sum([ways_makeable(d) for d in designs]))
