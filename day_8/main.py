'''Coding Challenge from https://adventofcode.com/2022/day/8'''
from pathlib import Path
import timeit
from itertools import takewhile

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return [[int(tree) for tree in list(tree_row)] for tree_row in file_input]

def part_1(tree_layout):

    visible_trees = 0
    transposed_tree_layout = [ list(column) for column in zip(*tree_layout)]

    for row_index,tree_row in enumerate(tree_layout):
        for column_index,tree in enumerate(tree_row):
            tree_height = tree

            #4 directions to check height
            #North
            if tree_height > max(transposed_tree_layout[column_index][:row_index],default=-1):
                visible_trees+=1
                continue

            #South
            if tree_height > max(transposed_tree_layout[column_index][row_index+1:],default=-1):
                visible_trees+=1
                continue

            #East
            if tree_height > max(tree_row[column_index+1:],default=-1):
                visible_trees+=1
                continue

            #West
            if tree_height > max(tree_row[:column_index],default=-1):
                visible_trees+=1
                continue

    return visible_trees

def part_2(tree_layout):

    scenic_scores = []
    transposed_tree_layout = [ list(column) for column in zip(*tree_layout)]

    for row_index,tree_row in enumerate(tree_layout):
        for column_index,tree in enumerate(tree_row):
            tree_height = tree
            north = 0
            south = 0
            east = 0
            west = 0

            #4 directions to check height
            #North
            north = len(take_until(tree_height, reversed(transposed_tree_layout[column_index][:row_index])))

            #South
            south = len(take_until(tree_height, transposed_tree_layout[column_index][row_index+1:]))

            #East
            east = len(take_until(tree_height, tree_row[column_index+1:]))

            #West
            west = len(take_until(tree_height, reversed(tree_row[:column_index])))

            scenic_scores.append(north*south*east*west)

    return max(scenic_scores, default=-1)

def take_until(value, tree_list):
    visible_trees = []
    for tree in tree_list:
        visible_trees.append(tree)
        if tree >= value:
            break

    return visible_trees

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
