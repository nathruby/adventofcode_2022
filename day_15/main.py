'''Coding Challenge from https://adventofcode.com/2022/day/15'''
from pathlib import Path
from collections import namedtuple
from time import sleep
import timeit

Point = namedtuple('Point', 'x y')

filepath = Path(__file__).with_name('input.txt')

def get_input():

    sensor_beacon = []

    with filepath.open('r', encoding='utf-8') as file:
        for line in file:
            locations_split = line.rstrip('\n').split(' ')

            sensor_x = int(locations_split[2].strip(',').strip('x='))
            sensor_y = int(locations_split[3].strip(':').strip('y='))

            beacon_x = int(locations_split[-2].strip(',').strip('x='))
            beacon_y = int(locations_split[-1].strip('y='))

            sensor_beacon.append([Point(sensor_x, sensor_y),Point(beacon_x, beacon_y)])

    return sensor_beacon

def part_1(sensor_beacon_pairs:list[list]):

    target_y = 2_000_000
    signal_ranges = []

    for sensor,beacon in sensor_beacon_pairs:

        distance = abs(sensor.x-beacon.x)\
            + abs(sensor.y-beacon.y)

        delta_y = abs(sensor.y - target_y)

        if delta_y <= distance:
            delta_x = distance - delta_y
            signal_ranges.append((sensor.x - delta_x, sensor.x + delta_x))

    signal_ranges.sort()

    signals = 0
    current_range = signal_ranges[0]

    for signal_range in signal_ranges[1:]:
        if signal_range[0] > current_range[1]:
            signals += current_range[1] - current_range[0]
            current_range = signal_range
        else:
            current_range = (min(current_range[0], signal_range[0])\
                , max(current_range[1], signal_range[1]))


    signals += current_range[1] - current_range[0]

    return signals

def part_2(sensor_beacon_pairs):

    range_limit = 4_000_000
    gap_x = 0
    gap_y = 0

    for row_index in range(range_limit+1):
        signal_ranges = []
        for sensor,beacon in sensor_beacon_pairs:
            distance = abs(sensor.x-beacon.x)\
                + abs(sensor.y-beacon.y)

            delta_y = abs(sensor.y - row_index)

            if delta_y <= distance:
                delta_x = distance - delta_y
                signal_ranges.append((max(0, sensor.x - delta_x)\
                    , min(sensor.x + delta_x, range_limit)))

        signal_ranges.sort()
        current_range = signal_ranges[0]
        joint_ranges = []
        for signal_range in signal_ranges[1:]:
            if signal_range[0] > current_range[1]:
                joint_ranges.append(current_range)
                current_range = signal_range
            else:
                current_range = (min(current_range[0], signal_range[0])\
                    , max(current_range[1], signal_range[1]))

        joint_ranges.append(current_range)

        first_range = joint_ranges[0]
        last_range = joint_ranges[-1]

        if min(first_range[0],0) > 0:
            gap_x = 0
            gap_y = row_index
            break
        elif max(last_range[1],range_limit) > range_limit:
            gap_x = range_limit
            gap_y = row_index
            break
        elif len(joint_ranges) > 1:
            gap_x = first_range[1]+1
            gap_y = row_index
            break

    return gap_x*4_000_000+gap_y

if __name__ == '__main__':
    file_input = get_input()
    part_1_results = part_1(file_input)
    part_2_results = part_2(file_input)

    #4737567,13267474686239
    print(part_1_results)
    print(part_2_results)

#     statement= '''
# file_input = get_input()
# part_1_results = part_1(file_input)
# part_2_results = part_2(file_input)
# '''
#     print(timeit.timeit(stmt=statement, globals=globals(), number=1000))
