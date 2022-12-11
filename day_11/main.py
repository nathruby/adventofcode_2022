'''Coding Challenge from https://adventofcode.com/2022/day/11'''
from pathlib import Path
from copy import deepcopy
from functools import reduce
from time import sleep

import timeit

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input

def part_1(head_pathing):

    monkeys:list = [
        {
            'levels': [89, 95, 92, 64, 87, 68],
            'operation': 'old * 11',
            'test': 2,
            'if_true': 7,
            'if_false': 4,
            'inspected_items': 0
        },
        {
            'levels': [87, 67],
            'operation': 'old + 1',
            'test': 13,
            'if_true': 3,
            'if_false': 6,
            'inspected_items': 0
        },
        {
            'levels': [95, 79, 92, 82, 60],
            'operation': 'old + 6',
            'test': 3,
            'if_true': 1,
            'if_false': 6,
            'inspected_items': 0
        },
        {
            'levels': [67, 97, 56],
            'operation': 'old * old',
            'test': 17,
            'if_true': 7,
            'if_false': 0,
            'inspected_items': 0
        },
        {
            'levels': [80, 68, 87, 94, 61, 59, 50, 68],
            'operation': 'old * 7',
            'test': 19,
            'if_true': 5,
            'if_false': 2,
            'inspected_items': 0
        },
        {
            'levels': [73, 51, 76, 59],
            'operation': 'old + 8',
            'test': 7,
            'if_true': 2,
            'if_false': 1,
            'inspected_items': 0
        },
        {
            'levels': [92],
            'operation': 'old + 5',
            'test': 11,
            'if_true': 3,
            'if_false': 0,
            'inspected_items': 0
        },
        {
            'levels': [99, 76, 78, 76, 79, 90, 89],
            'operation': 'old + 7',
            'test': 5,
            'if_true': 4,
            'if_false': 5,
            'inspected_items': 0
        }
    ]

    max_rounds: int = 20

    for _ in range(max_rounds):
        for monkey in monkeys:

            worry_levels = deepcopy(monkey['levels'])

            for worry_level in worry_levels:

                #adjust worry state
                left_side: int
                right_side: int

                equation = monkey['operation'].split(' ')

                if equation[0] == 'old':
                    left_side = worry_level
                else:
                    left_side = int(equation[0])

                if equation[2] == 'old':
                    right_side = worry_level
                else:
                    right_side = int(equation[2])

                if equation[1] == '+':
                    monkey['levels'][0] = left_side + right_side
                else:
                    monkey['levels'][0] = left_side * right_side

                #adjust monkey boredom
                monkey['levels'][0]//=3

                #test where to throw
                #true
                if monkey['levels'][0] % monkey['test'] == 0:
                    monkeys[monkey['if_true']]['levels'].append(monkey['levels'][0])
                #false
                else:
                    monkeys[monkey['if_false']]['levels'].append(monkey['levels'][0])

                del monkey['levels'][0]
                monkey['inspected_items']+=1

    results = sorted([monkey['inspected_items'] for monkey in monkeys], reverse=True)[:2]
    monkey_business: int = 1

    for result in results:
        monkey_business*=result
    return monkey_business

def part_2(head_pathing):
    
    monkeys:list = [
        {
            'levels': [89, 95, 92, 64, 87, 68],
            'operation': 'old * 11',
            'test': 2,
            'if_true': 7,
            'if_false': 4,
            'inspected_items': 0
        },
        {
            'levels': [87, 67],
            'operation': 'old + 1',
            'test': 13,
            'if_true': 3,
            'if_false': 6,
            'inspected_items': 0
        },
        {
            'levels': [95, 79, 92, 82, 60],
            'operation': 'old + 6',
            'test': 3,
            'if_true': 1,
            'if_false': 6,
            'inspected_items': 0
        },
        {
            'levels': [67, 97, 56],
            'operation': 'old * old',
            'test': 17,
            'if_true': 7,
            'if_false': 0,
            'inspected_items': 0
        },
        {
            'levels': [80, 68, 87, 94, 61, 59, 50, 68],
            'operation': 'old * 7',
            'test': 19,
            'if_true': 5,
            'if_false': 2,
            'inspected_items': 0
        },
        {
            'levels': [73, 51, 76, 59],
            'operation': 'old + 8',
            'test': 7,
            'if_true': 2,
            'if_false': 1,
            'inspected_items': 0
        },
        {
            'levels': [92],
            'operation': 'old + 5',
            'test': 11,
            'if_true': 3,
            'if_false': 0,
            'inspected_items': 0
        },
        {
            'levels': [99, 76, 78, 76, 79, 90, 89],
            'operation': 'old + 7',
            'test': 5,
            'if_true': 4,
            'if_false': 5,
            'inspected_items': 0
        }
    ]

    worry_cap = reduce(lambda x, y: x*y, [monkey['test'] for monkey in monkeys])

    max_rounds: int = 10*1000

    for _ in range(max_rounds):

        for monkey in monkeys:

            worry_levels = deepcopy(monkey['levels'])

            for worry_level in worry_levels:

                #adjust worry state
                left_side: int
                right_side: int

                equation = monkey['operation'].split(' ')

                if equation[0] == 'old':
                    left_side = worry_level
                else:
                    left_side = int(equation[0])

                if equation[2] == 'old':
                    right_side = worry_level
                else:
                    right_side = int(equation[2])

                if equation[1] == '+':
                    monkey['levels'][0] = left_side + right_side
                else:
                    monkey['levels'][0] = left_side * right_side

                #Cap the worry that satisfies all monkeys
                monkey['levels'][0]%=worry_cap

                #test where to throw
                #true
                if monkey['levels'][0] % monkey['test'] == 0:
                    #Cap the worry that satisfies all monkeys
                    monkeys[monkey['if_true']]['levels'].append(monkey['levels'][0])
                #false
                else:
                    monkeys[monkey['if_false']]['levels'].append(monkey['levels'][0])

                del monkey['levels'][0]
                monkey['inspected_items']+=1

    print([monkey['inspected_items'] for monkey in monkeys])
    results = sorted([monkey['inspected_items'] for monkey in monkeys], reverse=True)[:2]
    monkey_business: int = 1

    for result in results:
        monkey_business*=result

    return monkey_business

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
