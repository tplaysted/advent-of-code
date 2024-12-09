import re
import functools as ft

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

rules = [x.split('|') for x in re.findall("\\d+\\|\\d+", input)]
lookup = [[False for i in range(100)] for j in range(100)]  # high memory, O(1) comp

for rule in rules:
    lookup[int(rule[0])][int(rule[1])] = True

updates = [x.split(',') for x in re.findall("^\\d+,[\\d+,]*\\d+", input, flags=re.MULTILINE)]
updates = [[int(x) for x in update] for update in updates]

wrongs = []

for u in updates:
    n = len(u)
    index = [(i, j) for i in range(n - 1) for j in range(i + 1, n)]

    if not all([not lookup[u[j]][u[i]] for (i, j) in index]):
        wrongs.append(u)

def compare(a, b):
    if lookup[a][b]:
        return -1

    if lookup[b][a]:
        return 1

    return 0

wrongs = [sorted(w, key=ft.cmp_to_key(compare)) for w in wrongs]

total = sum([w[int((len(w)-1)/2)] for w in wrongs])
print(total)
