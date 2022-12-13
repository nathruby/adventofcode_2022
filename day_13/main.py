'''Coding Challenge from https://adventofcode.com/2022/day/12'''
from pathlib import Path
from time import sleep
import timeit

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [list(line.rstrip('\n')) for line in file]

    return file_input

def part_1(height_map):

    return 0

def part_2(height_map):

    return 0

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
