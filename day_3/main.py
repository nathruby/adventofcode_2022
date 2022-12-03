'''Coding Challenge from https://adventofcode.com/2022/day/3'''
from pathlib import Path

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input

def part_1(rucksacks):
    total_priority_score = 0

    for mixed_rucksack in rucksacks:
        rucksack_1 = mixed_rucksack[:int(len(mixed_rucksack)/2)]
        rucksack_2 = mixed_rucksack[int(len(mixed_rucksack)/2):]

        common_items = list(set(rucksack_1) & set(rucksack_2))
        total_priority_score+=convert_to_priority_score(common_items[0])

    return total_priority_score

def part_2(rucksacks):
    total_priority_score = 0

    for i in range(0, len(rucksacks), 3):
        rucksack_1 = rucksacks[i]
        rucksack_2 = rucksacks[i+1]
        rucksack_3 = rucksacks[i+2]

        common_items = list(set(rucksack_1) & set(rucksack_2) & set(rucksack_3))
        total_priority_score+=convert_to_priority_score(common_items[0])

    return total_priority_score

def convert_to_priority_score(item: str):
    '''
    Lowercase has a priority of at least 1 with a.
    Uppercase has a priority of at least 27 with A.
    '''

    if item.isupper():
        return ord(item)-38

    return ord(item)-96

if __name__ == '__main__':
    file_input = get_input()
    part_1_priority_score = part_1(file_input)
    part_2_priority_score = part_2(file_input)

    print(part_1_priority_score)
    print(part_2_priority_score)

#     statement= '''
# file_input = get_input()
# part_1_priority_score = part_1(file_input)
# part_2_priority_score = part_2(file_input)
# '''
#     print(timeit.timeit(stmt=statement, globals=globals(), number=1000))
