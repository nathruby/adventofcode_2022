'''Coding Challenge from https://adventofcode.com/2022/day/13'''
from pathlib import Path
from time import sleep
from itertools import zip_longest
from functools import cmp_to_key
from json import loads
import timeit

#TODO COME BACK TO TRY CLOSURE INSTEAD OF RECURSION

filepath = Path(__file__).with_name('input.txt')
BATCH_SIZE:int = 3

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input = [line.rstrip('\n').strip() for line in file]

    return file_input

def compare_if_ordered(left:list, right:list):

    if isinstance(left, list) and isinstance(right, list):
        for left_value, right_value in zip_longest(left, right):
            if left_value is None:
                return True

            if right_value is None:
                return False

            if isinstance(left_value, int) and isinstance(right_value, int):
                if left_value < right_value:
                    return True
                if right_value < left_value:
                    return False

            elif isinstance(left_value,int):
                is_ordered:bool = compare_if_ordered([left_value],right_value)
                if is_ordered is not None:
                    return is_ordered

            elif isinstance(right_value,int):
                is_ordered:bool = compare_if_ordered(left_value,[right_value])
                if is_ordered is not None:
                    return is_ordered

            else:
                is_ordered:bool = compare_if_ordered(left_value,right_value)
                if is_ordered is not None:
                    return is_ordered

    return None

def part_1(packet_input):

    packet_pairs:list[str] = []
    batch:list[str] = []

    for line in packet_input:
        batch.append(line.rstrip('\n').strip())

        if len(batch) >= BATCH_SIZE:
            packet_pairs.append(batch[0:2])
            batch = []

    packet_pairs.append(batch)

    pairs_in_right_order:list[int] = []
    for index,packet_pair in enumerate(packet_pairs):
        left = loads(packet_pair[0])
        right = loads(packet_pair[1])

        if compare_if_ordered(left, right):
            pairs_in_right_order.append(index+1)

    return sum(pairs_in_right_order)

def part_2(packet_input):

    part_two_packet_set:list[str] = [loads(packet) for packet in packet_input if packet != '']
    part_two_packet_set.append([[2]])
    part_two_packet_set.append([[6]])

    part_two_packet_set.sort(\
        key=cmp_to_key(lambda left,right: -1 if compare_if_ordered(left,right) else 1))

    divider_packet_two_location = part_two_packet_set.index([[2]])+1
    divider_packet_six_location = part_two_packet_set.index([[6]])+1
    return divider_packet_two_location*divider_packet_six_location


if __name__ == '__main__':
    file_input = get_input()
    part_1_results = part_1(file_input)
    part_2_results = part_2(file_input)

    #6272,22288
    print(part_1_results)
    print(part_2_results)

#     statement= '''
# file_input = get_input()
# part_1_results = part_1(file_input)
# part_2_results = part_2(file_input)
# '''
#     print(timeit.timeit(stmt=statement, globals=globals(), number=1000))
