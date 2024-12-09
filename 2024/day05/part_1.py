import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

rules = [x.split('|') for x in re.findall("\\d+\\|\\d+", input)]
lookup = [[True for i in range(100)] for j in range(100)]  # high memory, O(1) comp

for rule in rules:
    lookup[int(rule[0])][int(rule[1])] = False

updates = [x.split(',') for x in re.findall("^\\d+,[\\d+,]*\\d+", input, flags=re.MULTILINE)]
updates = [[int(x) for x in update] for update in updates]

total = 0

for u in updates:
    n = len(u)
    index = [(i, j) for i in range(n - 1) for j in range(i + 1, n)]

    if all([lookup[u[j]][u[i]] for (i, j) in index]):
        total += u[int((n-1)/2)]

print(total)
