'''Coding Challenge from https://adventofcode.com/2022/day/5'''
from pathlib import Path
import timeit

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input[10:]

def part_1(move_operations):

    stacks = [
        ['G', 'T', 'R', 'W'],
        ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W'],
        ['C', 'L', 'T', 'S', 'G', 'M'],
        ['J', 'H', 'D', 'M', 'W', 'R', 'F'],
        ['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J'],
        ['P', 'J', 'D', 'N', 'F', 'M', 'S'],
        ['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J'],
        ['R', 'T', 'B', 'W'],
        ['H', 'N', 'W', 'L', 'C'],
    ]

    for move_operation in move_operations:
        operations = move_operation.split(' ')

        removed_crates = stacks[int(operations[3])-1][-int(operations[1]):]
        del stacks[int(operations[3])-1][-int(operations[1]):]
        stacks[int(operations[5])-1] += removed_crates[::-1]


    return ''.join([stack[-1] for stack in stacks])

def part_2(move_operations):

    stacks = [
        ['G', 'T', 'R', 'W'],
        ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W'],
        ['C', 'L', 'T', 'S', 'G', 'M'],
        ['J', 'H', 'D', 'M', 'W', 'R', 'F'],
        ['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J'],
        ['P', 'J', 'D', 'N', 'F', 'M', 'S'],
        ['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J'],
        ['R', 'T', 'B', 'W'],
        ['H', 'N', 'W', 'L', 'C'],
    ]

    for move_operation in move_operations:
        operations = move_operation.split(' ')

        removed_crates = stacks[int(operations[3])-1][-int(operations[1]):]
        del stacks[int(operations[3])-1][-int(operations[1]):]
        stacks[int(operations[5])-1] += removed_crates

    return ''.join([stack[-1] if len(stack) > 0 else '' for stack in stacks])

if __name__ == '__main__':
    file_input = get_input()
    part_1_results = part_1(file_input)
    part_2_results = part_2(file_input)

    print(part_1_results)
    print(part_2_results)

#     statement= '''
# file_input = get_input()
# part_1_results = part_1(file_input)
# part_2_results = part_2(file_input)
# '''
#     print(timeit.timeit(stmt=statement, globals=globals(), number=1000))
