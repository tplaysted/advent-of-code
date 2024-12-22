from time import perf_counter

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

seeds = [int(x) for x in input.split('\n')[:-1]]

def diffs(input):  # diffs on a list
    for i in range(1, len(input)):
        yield input[i] - input[i-1]

def next(a):
    x = ((a << 6) ^ a) & (2 ** 24 - 1)  # step 1
    y = ((x >> 5) ^ x) & (2 ** 24 - 1)  # step 2
    return ((y << 11) ^ y) & (2 ** 24 - 1)  # step 3

def changes_to_prices(a, n):  # a dict of changes to prices for a given starting number
    secrets = [0 for _ in range(n + 1)]
    secrets[0] = a
    changes = {}

    for i in range(1, n + 1):
        secrets[i] = next(secrets[i-1])

    flucs = [x for x in diffs([x % 10 for x in secrets])]  # diffs but a different name

    for i in range(0, n-4):
        change = tuple(flucs[i:i+4])
        price = secrets[i+4] % 10

        if change not in changes:  # only the first price is stored
            changes[change] = price

    return changes

change_scores = {}  # keeps track of a change set and the corresponding TOTAL profit from that score

tic = perf_counter()
for seed in seeds:
    changes = changes_to_prices(seed, 2001)  # this off by one had me MESSED UP MAN

    for change in changes:
        if change in change_scores:
            change_scores[change] += changes[change]  # why did i choose these names
        else:
            change_scores[change] = changes[change]

best = max(change_scores, key=lambda x: change_scores[x])
best_prof = change_scores[best]
toc = perf_counter()

print(best, ':', best_prof)
print('executed in', int((toc - tic) * 1000), ' ms')
