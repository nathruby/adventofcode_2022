'''Coding Challenge from https://adventofcode.com/2022/day/8'''
from pathlib import Path
import timeit

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input

def part_1(assignment_pairs):

    total_subsets = 0

    return total_subsets

def part_2(assignment_pairs):
    total_intersects = 0
    
    return total_intersects

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
