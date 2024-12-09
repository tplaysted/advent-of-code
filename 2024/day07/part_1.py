import re

input_path = 'input.txt'

with open(input_path) as file:
    input = file.read()

lines = input.split('\n')
lines = lines[0:len(lines)-1]

def get_result(line):
    output = [int(x) for x in re.findall("(\\d+):", line)]
    output = output[0]

    operands = [int(x) for x in re.findall(" \\d+", line)]

    for i in range(2 ** (len(operands) - 1)):
        op_string = list('{0:0b}'.format(i))
        op_string = ['0' for _ in range((len(operands)-1) - len(op_string))] + op_string

        sum = operands[0]

        for i in range(1, len(operands)):
            op = operands[i]

            if op_string[i-1] == '0':
                sum += op
            else:
                sum *= op

        if sum == output:
            return output

    return 0

print(sum([get_result(line) for line in lines]))
