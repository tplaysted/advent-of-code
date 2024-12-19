from functools import cache  # we will recompute the same designs lots of times

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
blocks = lines[0].split(', ')
designs = lines[2:-2]

@cache
def is_makeable(design):
    if design == '':
        return True

    for i in range(1, len(design) + 1):
        part, right = design[0:i], design[i:len(design)]

        if (part in blocks) and is_makeable(right):
            return True

    return False

print(sum([1 for d in designs if is_makeable(d)]))
