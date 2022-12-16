'''Coding Challenge from https://adventofcode.com/2022/day/16'''
from pathlib import Path
from time import sleep
import timeit

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input = [line.rstrip('\n') for line in file]

    return file_input

def part_1(rock_formations):
    number_of_sand_placed = 0

    return number_of_sand_placed

def part_2(rock_formation):

    number_of_sand_placed = 0

    return number_of_sand_placed

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
