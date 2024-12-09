def find_open_brackets(input):
    return [index for (index, c) in enumerate(input) if c == '(']

def find_closed_brackets(input):
    return [index for (index, c) in enumerate(input) if c == ')']

def preceeded_by_mul(input, index):
    if index < 4:
        return False

    if input[index - 3:index] == 'mul':
        return True

    return False

def get_valid_num_input(input, bracket_index):
    valid_pairs = []

    for index in bracket_index:
        internal = input[index[0]+1:index[1]]
        internal = internal.split(',')

        if len(internal) != 2:
            continue

        if internal[0].isnumeric() and internal[1].isnumeric():
            valid_pairs.append((int(internal[0]), int(internal[1])))

    return valid_pairs

def process_input(input_path):
    with open(input_path, 'r') as file:
        input = file.read()

    # Valid pair of brackets
    o = [(i, '(') for i in find_open_brackets(input)]
    c = [(i, ')') for i in find_closed_brackets(input)]
    brackets = o + c
    brackets.sort(key=lambda x: x[0])

    valid_bracket_index = []

    for i in range(len(brackets) - 1):
        if brackets[i][1] == '(' and brackets[i+1][1] == ')':
            valid_bracket_index.append((brackets[i][0], brackets[i+1][0]))

    # Is preceeded by a 'mul'
    valid_bracket_index = list(filter(lambda x: preceeded_by_mul(input, x[0]), valid_bracket_index))

    # Contains a valid numerical input
    pairs = get_valid_num_input(input, valid_bracket_index)

    # Summation

    return sum([a * b for (a,b) in pairs])

if __name__ == "__main__":
    print(process_input('input.txt'))
