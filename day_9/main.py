'''Coding Challenge from https://adventofcode.com/2022/day/9'''
from pathlib import Path
import timeit
from itertools import takewhile

filepath = Path(__file__).with_name('input.txt')

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

    tail_point_visits = set()
    head = Knot(0,0)
    tail = Knot(0,0)

    tail_point_visits.add(tail.get_coordinates())

    for head_move in head_pathing:
        direction, move = head_move.split(' ')

        if direction == 'U':
            for _ in range(0, int(move)):
                head.y+=1 #move head
                move_tail(head, tail)
                tail_point_visits.add(tail.get_coordinates())

        if direction == 'D':
            for _ in range(0, int(move)):
                head.y-=1 #move head
                move_tail(head, tail)
                tail_point_visits.add(tail.get_coordinates())

        if direction == 'L':
            for _ in range(0, int(move)):
                head.x-=1 #move head
                move_tail(head, tail)
                tail_point_visits.add(tail.get_coordinates())

        if direction == 'R':
            for _ in range(0, int(move)):
                head.x+=1 #move head
                move_tail(head, tail)
                tail_point_visits.add(tail.get_coordinates())

    return len(tail_point_visits)

def part_2(head_pathing):

    tail_point_visits = set()
    head = Knot(0,0)
    tails = [Knot(0,0) for _ in range(9)]
    tail_point_visits.add(tails[0].get_coordinates())

    for head_move in head_pathing:
        direction, move = head_move.split(' ')

        if direction == 'U':
            for _ in range(0, int(move)):
                head.y+=1 #move head
                move_tail(head, tails[0])

                for tail_index in range(0,len(tails)-1):
                    move_tail(tails[tail_index],tails[tail_index+1])

                tail_point_visits.add(tails[-1].get_coordinates())

        if direction == 'D':
            for _ in range(0, int(move)):
                head.y-=1 #move head
                move_tail(head, tails[0])

                for tail_index in range(0,len(tails)-1):
                    move_tail(tails[tail_index],tails[tail_index+1])

                tail_point_visits.add(tails[-1].get_coordinates())

        if direction == 'L':
            for _ in range(0, int(move)):
                head.x-=1 #move head
                move_tail(head, tails[0])

                for tail_index in range(0,len(tails)-1):
                    move_tail(tails[tail_index],tails[tail_index+1])

                tail_point_visits.add(tails[-1].get_coordinates())

        if direction == 'R':
            for _ in range(0, int(move)):
                head.x+=1 #move head
                move_tail(head, tails[0])

                for tail_index in range(0,len(tails)-1):
                    move_tail(tails[tail_index],tails[tail_index+1])

                tail_point_visits.add(tails[-1].get_coordinates())

    return len(tail_point_visits)

def move_tail(head: Knot, tail: Knot):

    delta_x = head.x - tail.x
    delta_y = head.y - tail.y

    #Tail moves up
    if delta_y > 1:
        tail.y+=1
        if delta_x > 0:
            tail.x+=1
        elif delta_x < 0:
            tail.x-=1

    #Tail moves down
    elif delta_y < -1:
        tail.y-=1
        if delta_x > 0:
            tail.x+=1
        elif delta_x < 0:
            tail.x-=1

    #Tail moves left
    elif delta_x < -1:
        tail.x-=1
        if delta_y > 0:
            tail.y+=1
        elif delta_y < 0:
            tail.y-=1

    #Tail moves right
    elif delta_x > 1:
        tail.x+=1
        if delta_y > 0:
            tail.y+=1
        elif delta_y < 0:
            tail.y-=1

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
