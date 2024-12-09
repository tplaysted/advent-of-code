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

    for i in range(3 ** (len(operands) - 1)):
        op_string = [(i // (3 ** k)) % 3 for k in range(len(operands) - 1)]
        sum = operands[0]

        for i in range(1, len(operands)):
            op = operands[i]

            if op_string[i-1] == 0:
                sum += op
            elif op_string[i-1] == 1:
                sum *= op
            else:
                sum = int(str(sum) + str(op))

        if sum == output:
            return output

    return 0

# print(get_result(lines[7]))
print(sum([get_result(line) for line in lines]))
