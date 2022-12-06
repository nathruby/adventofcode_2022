'''Coding Challenge from https://adventofcode.com/2022/day/6'''
from pathlib import Path
import timeit

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input[0]

def find_starting_marker(input_stream, distinct_values):

    starting_marker: int

    for ending_index in range(distinct_values, len(input_stream)+1):
        starting_marker = ending_index

        if len(set(input_stream[ending_index-distinct_values:ending_index]))==distinct_values:
            break

    return starting_marker

if __name__ == '__main__':
    file_input = get_input()
    part_1_results = find_starting_marker(file_input, 4) #Part 1: End of Packet
    part_2_results = find_starting_marker(file_input, 14) #Part 2: End of Message

    print(part_1_results)
    print(part_2_results)

#     statement= '''
# file_input = get_input()
# part_1_results = find_starting_marker(file_input, 4)
# part_2_results = find_starting_marker(file_input, 14)
# '''
#     print(timeit.timeit(stmt=statement, globals=globals(), number=1000))
