'''Coding Challenge from https://adventofcode.com/2022/day/4'''
from pathlib import Path
import timeit

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input[0]

def part_1(input_stream):
    start_of_packet_marker = 3 #best cast scenario, the first 4 characters are unique

    for beginning_index in range(len(input_stream)+1):
        start_of_packet_marker+=1

        if len(set(input_stream[beginning_index:beginning_index+4]))==4:
            return start_of_packet_marker

    return start_of_packet_marker

def part_2(input_stream):

    start_of_message_marker = 13 #best cast scenario, the first 13 characters are unique

    for beginning_index in range(len(input_stream)+1):
        start_of_message_marker+=1
        
        if len(set(input_stream[beginning_index:beginning_index+13]))==13:
            return start_of_message_marker

    return start_of_message_marker

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
