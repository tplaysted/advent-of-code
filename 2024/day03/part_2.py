import re

input_path = 'input.txt'

with open(input_path, 'r') as file:
    input = file.read()

valid_strings = re.findall("(mul\\(\\d+\\,\\d+\\)|do\\(\\)|don't\\(\\))", input)

total = 0
enabled = True

total = 0

for match in valid_strings:
    if match == "don't()":
        enabled = False
        continue

    if match == "do()":
        enabled = True
        continue

    if not enabled:
        continue

    nums = [x.split(',') for x in re.findall("\\d+", match)]
    total += int(nums[0][0]) * int(nums[1][0])

print(total)
