'''Coding Challenge from https://adventofcode.com/2022/day/9'''
from pathlib import Path
from time import sleep
import timeit

filepath = Path(__file__).with_name('input.txt')
PRINT_MODE = False
ANIMATE_MODE = False

class Knot():
    x = 0
    y = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_coordinates(self):
        return tuple([self.x,self.y])

    def __str__(self) -> str:
        return f'X: {self.x}, Y: {self.y}'

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input

def part_1(head_pathing):

    tail_points_visited = set()
    head = Knot(0,0)
    tail = Knot(0,0)

    tail_points_visited.add(tail.get_coordinates())

    for head_move in head_pathing:
        direction, move = head_move.split(' ')

        for _ in range(int(move)):

            if direction == 'U':
                head.y+=1 #move head
            elif direction == 'D':
                head.y-=1 #move head
            elif direction == 'L':
                head.x-=1 #move head
            elif direction == 'R':
                head.x+=1 #move head

            move_tail(head,tail)

            tail_points_visited.add(tail.get_coordinates())

    return len(tail_points_visited)

def part_2(head_pathing):

    if ANIMATE_MODE:
        print('\n'.join([''.join(['.' for _ in range(-100,101)]) for _ in range(-50,51)]))

    tail_points_visited = set()
    knots = [Knot(0,0) for _ in range(10)]
    tail_points_visited.add(knots[-1].get_coordinates())

    if ANIMATE_MODE:
        print_rope_moving(knots, tail_points_visited)

    for head_move in head_pathing:
        direction, move = head_move.split(' ')

        for _ in range(int(move)):

            if direction == 'U':
                knots[0].y+=1 #move head
            elif direction == 'D':
                knots[0].y-=1 #move head
            elif direction == 'L':
                knots[0].x-=1 #move head
            elif direction == 'R':
                knots[0].x+=1 #move head

            for tail_index in range(0,len(knots)-1):
                move_tail(knots[tail_index],knots[tail_index+1])

            tail_points_visited.add(knots[-1].get_coordinates())
            if ANIMATE_MODE:
                print_rope_moving(knots, tail_points_visited)

    if PRINT_MODE or ANIMATE_MODE:
        print_rope_moving(knots, tail_points_visited, True)

    return len(tail_points_visited)

def move_tail(head: Knot, tail: Knot):

    delta_x = head.x - tail.x
    delta_y = head.y - tail.y

    #Tail moves up or down
    if abs(delta_y) > 1:
        tail.y+=delta_y//2
        if abs(delta_x) > 0:
            tail.x+=delta_x//abs(delta_x)

    #Tail moves left or right
    elif abs(delta_x) > 1:
        tail.x+=delta_x//2
        if abs(delta_y) > 0:
            tail.y+=delta_y//abs(delta_y)

def print_rope_moving(knots: list[Knot], tail_points_visited: set[Knot], is_complete: bool=False):
    sleep(0.1)
    print_grid = []

    for y in range(50, -51, -1):
        row = []
        for x in range(-100, 101):
            column = '.'
            if (x,y) in tail_points_visited:
                column = '#'

            if not is_complete:
                if x == knots[9].x and y == knots[9].y:
                    column = '9'
                if x == knots[8].x and y == knots[8].y:
                    column = '8'
                if x == knots[7].x and y == knots[7].y:
                    column = '7'
                if x == knots[6].x and y == knots[6].y:
                    column = '6'
                if x == knots[5].x and y == knots[5].y:
                    column = '5'
                if x == knots[4].x and y == knots[4].y:
                    column = '4'
                if x == knots[3].x and y == knots[3].y:
                    column = '3'
                if x == knots[2].x and y == knots[2].y:
                    column = '2'
                if x == knots[1].x and y == knots[1].y:
                    column = '1'
                if x == knots[0].x and y == knots[0].y:
                    column = 'H'

            row.append(column)

        print_grid.append(row)

    print('\033c')
    print('\n'.join([''.join(row) for row in print_grid]))

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
