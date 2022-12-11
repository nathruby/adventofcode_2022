'''Coding Challenge from https://adventofcode.com/2022/day/11'''
from pathlib import Path
from copy import deepcopy
from functools import reduce
from time import sleep
import timeit

filepath = Path(__file__).with_name('input.txt')
BATCH_SIZE = 7

class Operation():
    left_side:str
    right_side:str
    operator:str

    def __init__(self, operation_string:str) -> None:

        operation_list = operation_string.split(' ')
        self.left_side = operation_list[2]
        self.right_side = operation_list[4]
        self.operator = operation_list[3]

class Monkey():
    worry_levels:list[int]
    operation: Operation
    test:int
    monkey_if_true:int
    monkey_if_false:int
    inspected_items:int = 0

    def __init__(self, monkey_details:list[list[str]]) -> None:
        self.worry_levels = [int(worry_level.strip()) \
            for worry_level in monkey_details[1].lstrip('Starting items:').split(',')]

        self.operation = Operation(monkey_details[2].lstrip('Operation:').strip())
        self.test = int(monkey_details[3].split(' ')[-1])
        self.monkey_if_true = int(monkey_details[4].split(' ')[-1])
        self.monkey_if_false = int(monkey_details[5].split(' ')[-1])

def get_input():

    monkeys:list[Monkey] = []
    batch:list[str] = []

    with filepath.open('r', encoding='utf-8') as file:
        for line in file:
            batch.append(line.rstrip('\n').strip())

            if len(batch) >= BATCH_SIZE:
                monkeys.append(Monkey(batch))
                batch = []

    monkeys.append(Monkey(batch))
    return monkeys

def part_1(monkey_input):

    monkeys:list[Monkey] = deepcopy(monkey_input)
    max_rounds: int = 20

    for _ in range(max_rounds):

        monkey:Monkey
        for monkey in monkeys:

            worry_levels = deepcopy(monkey.worry_levels)

            for worry_level in worry_levels:

                #adjust worry state
                left_side: int
                right_side: int

                if monkey.operation.left_side == 'old':
                    left_side = worry_level
                else:
                    left_side = int(monkey.operation.left_side)

                if monkey.operation.right_side == 'old':
                    right_side = worry_level
                else:
                    right_side = int(monkey.operation.right_side)

                if monkey.operation.operator == '+':
                    monkey.worry_levels[0]  = left_side + right_side
                else:
                    monkey.worry_levels[0]  = left_side * right_side

                #adjust monkey boredom
                monkey.worry_levels[0]//=3

                #test where to throw
                #true
                if monkey.worry_levels[0] % monkey.test == 0:
                    monkeys[monkey.monkey_if_true].worry_levels.append(monkey.worry_levels[0])
                #false
                else:
                    monkeys[monkey.monkey_if_false].worry_levels.append(monkey.worry_levels[0])

                del monkey.worry_levels[0]
                monkey.inspected_items+=1

    results = sorted([monkey.inspected_items for monkey in monkeys], reverse=True)[:2]
    monkey_business: int = 1

    for result in results:
        monkey_business*=result
    return monkey_business

def part_2(monkey_input):

    monkeys:list[Monkey] = deepcopy(monkey_input)
    max_rounds: int = 10*1000
    worry_cap = reduce(lambda x, y: x*y, [monkey.test for monkey in monkeys])

    for _ in range(max_rounds):

        monkey:Monkey
        for monkey in monkeys:

            worry_levels = deepcopy(monkey.worry_levels)

            for worry_level in worry_levels:

                #adjust worry state
                left_side: int
                right_side: int

                if monkey.operation.left_side == 'old':
                    left_side = worry_level
                else:
                    left_side = int(monkey.operation.left_side)

                if monkey.operation.right_side == 'old':
                    right_side = worry_level
                else:
                    right_side = int(monkey.operation.right_side)

                if monkey.operation.operator == '+':
                    monkey.worry_levels[0]  = left_side + right_side
                else:
                    monkey.worry_levels[0]  = left_side * right_side

                #adjust monkey boredom
                monkey.worry_levels[0]%=worry_cap

                #test where to throw
                #true
                if monkey.worry_levels[0] % monkey.test == 0:
                    monkeys[monkey.monkey_if_true].worry_levels.append(monkey.worry_levels[0])
                #false
                else:
                    monkeys[monkey.monkey_if_false].worry_levels.append(monkey.worry_levels[0])

                del monkey.worry_levels[0]
                monkey.inspected_items+=1

    results = sorted([monkey.inspected_items for monkey in monkeys], reverse=True)[:2]
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
