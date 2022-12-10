'''Coding Challenge from https://adventofcode.com/2022/day/10'''
from pathlib import Path
from time import sleep

import timeit

ANIMATE_MODE = False

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input

def part_1(operations):

    signal_strengths = []
    register_x = 1
    cycle = 1

    for operation in operations:
        opcode = operation.split(' ')
        cycle_countdown = 0

        if opcode[0] == 'noop':
            cycle_countdown=1

        if opcode[0] == 'addx':
            cycle_countdown=2

        while cycle_countdown > 0:
            cycle_countdown-=1
            cycle+=1

            if opcode[0] == 'addx' and cycle_countdown == 0:
                register_x+=int(opcode[1])

            if cycle == 20+40*len(signal_strengths):
                signal_strengths.append(register_x*cycle)

    return sum(signal_strengths)

def part_2(operations):
    register_x = 1
    cycle = 1
    current_crt_row = ''
    sprite_display = ['.' * 40 for _ in range(6)]

    if ANIMATE_MODE:
        print_solution(register_x, sprite_display)

    for operation in operations:
        opcode = operation.split(' ')
        cycle_countdown = 0

        if opcode[0] == 'noop':
            cycle_countdown=1

        if opcode[0] == 'addx':
            cycle_countdown=2

        while cycle_countdown > 0:

            #During Cycle
            if register_x-1 <= (cycle-1)%40 <= register_x+1:
                current_crt_row+='#'
            else:
                current_crt_row+='.'


            if cycle%40 == 0:
                sprite_display[(cycle//40)-1] = current_crt_row
                current_crt_row=''
            else:
                sprite_display[cycle//40] = current_crt_row + '.'*(40 - len(current_crt_row))

            if ANIMATE_MODE:
                print_solution(register_x, sprite_display)

            #End of a cycle
            cycle+=1
            cycle_countdown-=1

            if opcode[0] == 'addx' and cycle_countdown == 0:
                register_x+=int(opcode[1])

    print_solution(register_x, sprite_display)

def print_solution(register, sprite_display):
    sleep(0.1)
    blank_row = '.'*40
    sprite_position = ''

    if register == -1:
        sprite_position = '#'*1 + '.'*39
    elif register == 0:
        sprite_position = '##' + '.'*38
    elif 1 < register <= 38:
        sprite_position = '###'.join([blank_row[:register-1],blank_row[register+2:]])
    elif register == 39:
        sprite_position = '.'*38 + '##'
    elif register == 40:
        sprite_position = '.'*39 + '#'
    else:
        sprite_position = '.'*40

    print('\033c')
    print(sprite_position, register, '\n')
    print('\n'.join(row for row in sprite_display))

if __name__ == '__main__':
    file_input = get_input()
    part_1_results = part_1(file_input)
    part_2(file_input)

    print(part_1_results)
#     statement= '''
# file_input = get_input()
# part_1_results = part_1(file_input)
# '''
#     print(timeit.timeit(stmt=statement, globals=globals(), number=1000))
