input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

seeds = [int(x) for x in input.split('\n')[:-1]]

def next(a):
    x = ((a << 6) ^ a) & (2 ** 24 - 1)  # step 1
    y = ((x >> 5) ^ x) & (2 ** 24 - 1)  # step 2
    return ((y << 11) ^ y) & (2 ** 24 - 1)  # step 3

def generate(a, n):
    x = a
    for _ in range(n):
        x = next(x)

    return x

print(sum([generate(s, 2000) for s in seeds]))
