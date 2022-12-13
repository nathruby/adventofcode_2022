'''Coding Challenge from https://adventofcode.com/2022/day/12'''
from pathlib import Path
from time import sleep
from copy import deepcopy
from collections import namedtuple
import timeit

filepath = Path(__file__).with_name('input.txt')

ANIMATED_MODE: bool = False
Point = namedtuple('Point', 'x y')

class Terrain():
    height_map:list[str]
    width:int
    height:int
    start:Point
    destination:Point
    moves:list[int]
    visited_map:list[str]
    part_2:bool = False

    def __init__(self, data, width) -> None:
        self.height_map = data
        self.width = width
        self.height = len(data)//width

        i = self.height_map.index('S')
        self.start = Point(i%self.width,i//self.width)

        i = self.height_map.index('E')
        self.destination = Point(i%self.width,i//self.width)

        self.moves = [-1]*len(self.height_map)
        self.visited_map = ['.']*len(self.height_map)

    def print_map(self):
        for i in range(0,self.height):
            print(self.height_map[i*self.width:(i+1)*self.width])

    def print_moves(self):
        for i in range(0,self.height):
            print( self.moves[i*self.width:(i+1)*self.width])

    def print_visited_map(self):
        print('\033c')
        temp_map = []
        for i in range(0,self.height):
            temp_map.append(''.join(self.visited_map[i*self.width:(i+1)*self.width]))

        print('\n'.join(row for row in temp_map))

    def mark_point_visited(self, position):
        mountain_height = self.height_map[position.y*self.width+position.x]
        self.visited_map[position.y*self.width+position.x] = mountain_height

    def total_cost(self):
        i = self.height_map.index('E')
        return self.moves[i]

    def get_mountain_height(self, position:Point, offset_x = 0, offset_y = 0):
        x = position.x + offset_x
        if x < 0 or x >= self.width:
            return None

        y = position.y + offset_y
        if y < 0 or y >= self.height:
            return None

        mountain_height = self.height_map[y*self.width+x]
        if mountain_height == 'S':
            mountain_height = 'a'
        if mountain_height == 'E':
            mountain_height = 'z'

        return mountain_height

    def set_move_cost(self, position, cost):
        i = position.y*self.width+position.x

        #is the move cost at position less than the current moves to get to same position
        if self.moves[i] == -1 or cost < self.moves[i]:
            self.moves[i] = cost
            return True

        return False

    def to_position(self, index):
        return Point(index%self.width, index//self.width)

    def find_path(self):
        to_visit = [(self.start, 0)]

        if self.part_2:
            to_visit += [(self.to_position(a_index),0) \
                for a_index,a_location in enumerate(self.height_map) if a_location == 'a']

        while len(to_visit) > 0:
            position,cost = to_visit.pop(0)

            if not self.part_2 and ANIMATED_MODE:
                self.mark_point_visited(position)
                self.print_visited_map()

            if self.set_move_cost(position,cost):
                mountain_height = self.get_mountain_height(position)

                if position.x == self.destination.x and position.y == self.destination.y:
                    return

                #go north
                north_position = self.get_mountain_height(position, 0, -1)
                if north_position is not None\
                    and ord(north_position)-ord(mountain_height) <= 1:
                    to_visit.append((Point(position.x, position.y-1),cost+1))

                south_position = self.get_mountain_height(position, 0, 1)
                #go south
                if south_position is not None\
                    and ord(south_position)-ord(mountain_height) <= 1:
                    to_visit.append((Point(position.x, position.y+1),cost+1))


                east_position = self.get_mountain_height(position, -1, 0)
                #go east
                if east_position is not None\
                    and ord(east_position)-ord(mountain_height) <= 1:
                    to_visit.append((Point(position.x-1, position.y),cost+1))


                west_position = self.get_mountain_height(position, 1, 0)
                #go wests
                if west_position is not None\
                    and ord(west_position)-ord(mountain_height) <= 1:
                    to_visit.append((Point(position.x+1, position.y),cost+1))

def get_input():

    width = 0
    file_input = []
    with filepath.open('r', encoding='utf-8') as file:
        for line in file:
        # file_input =  [list(line.rstrip('\n')) for line in file]
            line = line.strip()
            width = len(line)
            file_input.extend(line)


    terrain = Terrain(file_input, width)
    return terrain

def part_1(height_map:Terrain):

    part_one_height_map:Terrain = deepcopy(height_map)

    if ANIMATED_MODE:
        part_one_height_map.print_visited_map()
        sleep(2.0)

    part_one_height_map.find_path()
    return part_one_height_map.total_cost()

def part_2(height_map:Terrain):

    part_two_height_map:Terrain = deepcopy(height_map)
    part_two_height_map.part_2 = True

    part_two_height_map.find_path()
    return part_two_height_map.total_cost()

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
