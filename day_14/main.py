'''Coding Challenge from https://adventofcode.com/2022/day/14'''
from pathlib import Path
from time import sleep
import timeit

filepath = Path(__file__).with_name('input.txt')

def create_cave_map(rock_formations) -> dict:
    cave_map = {}

    #Draw Sand Source
    cave_map[(500,0)] = '+'

    #Draw Rocks
    for rock_formation_directions in rock_formations:
        rock_lines = [rock_line.strip() for rock_line in rock_formation_directions.split('->')]

        for index in range(0,len(rock_lines)-1):
            start = [int(coordinate) for coordinate in rock_lines[index].strip().split(',')]
            end = [int(coordinate) for coordinate in rock_lines[index+1].strip().split(',')]

            if start[0] > end[0]:
                offset = start[0] - end[0]

                for offset_x in range(offset+1):
                    cave_map[(start[0]-offset_x, start[1])] = '#'
            elif start[0] < end[0]:
                offset = end[0]-start[0]

                for offset_x in range(offset+1):
                    cave_map[(start[0]+offset_x, start[1])] = '#'
            elif start[1] > end[1]:
                offset = start[1] - end[1]

                for offset_y in range(offset+1):
                    cave_map[(start[0], start[1]-offset_y)] = '#'
            elif start[1] < end[1]:
                offset = end[1]-start[1]

                for offset_y in range(offset+1):
                    cave_map[(start[0], start[1]+offset_y)] = '#'

    return cave_map

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input = [line.rstrip('\n').strip() for line in file]

    return file_input

def part_1(rock_formations):
    cave_map = create_cave_map(rock_formations)

    max_depth = max(key[1] for key in cave_map)

    sand_source = (500,0)
    sand_falling_forever = False
    number_of_sand_placed = 0

    #Draw Sand
    while not sand_falling_forever:

        sand_placed = False
        sand_location = list(sand_source)

        while not sand_placed and not sand_falling_forever:

            #Sand falls deeper than the deepest rock
            if sand_location[1] >= max_depth:
                sand_falling_forever = True
            #Still air, keep falling
            if (sand_location[0], sand_location[1]+1) not in cave_map:
                sand_location[1]+=1
            #Fall until hit rock or sand
            else:
                #check if it can drop down left
                if (sand_location[0]-1, sand_location[1]+1) not in cave_map:
                    sand_location[0]-=1
                    sand_location[1]+=1
                #check if it can drop down right
                elif (sand_location[0]+1, sand_location[1]+1) not in cave_map:
                    sand_location[0]+=1
                    sand_location[1]+=1
                #cannot settle anywhere else
                else:
                    cave_map[(sand_location[0], sand_location[1])] = 'o'
                    sand_placed = True
                    number_of_sand_placed+=1

    return number_of_sand_placed

def part_2(rock_formation):

    cave_map = create_cave_map(rock_formation)
    max_depth = max( key[1] for key in cave_map)+2

    sand_source = (500,0)
    sand_blocked = False
    number_of_sand_placed = 0

    #Draw Floor
    for x in range(-9999,10000):
        cave_map[(x, max_depth)] = '#'

    #Draw Sand
    while not sand_blocked:

        sand_placed = False
        sand_location = list(sand_source)

        while not sand_placed and not sand_blocked:

            #Still air, keep falling
            if (sand_location[0], sand_location[1]+1) not in cave_map:
                sand_location[1]+=1
            #Fall until hit rock or sand
            else:
                #check if it can drop down left
                if (sand_location[0]-1, sand_location[1]+1) not in cave_map:
                    sand_location[0]-=1
                    sand_location[1]+=1
                #check if it can drop down right
                elif (sand_location[0]+1, sand_location[1]+1) not in cave_map:
                    sand_location[0]+=1
                    sand_location[1]+=1
                #check if covering the hole
                elif (sand_location[0], sand_location[1]) == sand_source:
                    number_of_sand_placed+=1
                    sand_blocked = True
                    sand_placed = True
                #cannot settle anywhere else
                else:
                    cave_map[(sand_location[0], sand_location[1])] = 'o'
                    sand_placed = True
                    number_of_sand_placed+=1

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
