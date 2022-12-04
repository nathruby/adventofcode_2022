'''Coding Challenge from https://adventofcode.com/2022/day/4'''
from pathlib import Path

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input

def part_1(assignment_pairs):
    
    total_overlaps = 0

    for assignment_pair in assignment_pairs:
        assignment_pair = assignment_pair.split(',')
        group_1_range = assignment_pair[0].split('-')
        group_2_range = assignment_pair[1].split('-')

        group_1 = { i for i in range(int(group_1_range[0]), int(group_1_range[1])+1)}
        group_2 = { i for i in range(int(group_2_range[0]), int(group_2_range[1])+1)}

        if group_1.issubset(group_2) or group_2.issubset(group_1):
            total_overlaps+=1

    return total_overlaps

def part_2(assignment_pairs):
    total_overlaps = 0

    for assignment_pair in assignment_pairs:
        assignment_pair = assignment_pair.split(',')
        group_1_range = assignment_pair[0].split('-')
        group_2_range = assignment_pair[1].split('-')

        group_1 = set( i for i in range(int(group_1_range[0]), int(group_1_range[1])+1))
        group_2 = set( i for i in range(int(group_2_range[0]), int(group_2_range[1])+1))

        if group_1 & group_2:
            total_overlaps+=1

    return total_overlaps

if __name__ == '__main__':
    file_input = get_input()
    part_1_results = part_1(file_input)
    part_2_results = part_2(file_input)

    print(part_1_results)
    print(part_2_results)
#     statement= '''
# file_input = get_input()
# part_1_priority_score = part_1(file_input)
# part_2_priority_score = part_2(file_input)
# '''
#     print(timeit.timeit(stmt=statement, globals=globals(), number=1000))
