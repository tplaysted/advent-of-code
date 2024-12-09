import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines.pop() # last line blank

n = len(lines)

cols = [''.join([line[i] for line in lines]) for i in range(n)]

diags_down = [''.join([lines[a+i][i] for i in range(n-a)]) for a in range(n)]
diags_down += [''.join([lines[i][a+i] for i in range(n-a)]) for a in range(1, n)]

diags_up = [''.join([lines[n-a-i-1][i] for i in range(n-a)]) for a in range(n)]
diags_up += [''.join([lines[n-i-1][a+i] for i in range(n-a)]) for a in range(1, n)]

total = 0
total += sum(len(re.findall('(?=XMAS|SAMX)', x)) for x in lines)
total += sum(len(re.findall('(?=XMAS|SAMX)', x)) for x in cols)
total += sum(len(re.findall('(?=XMAS|SAMX)', x)) for x in diags_down)
total += sum(len(re.findall('(?=XMAS|SAMX)', x)) for x in diags_up)

print(total)
