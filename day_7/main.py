'''Coding Challenge from https://adventofcode.com/2022/day/4'''
from pathlib import Path
import timeit

filepath = Path(__file__).with_name('input.txt')

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input

def create_directory(command_input):

    directory_tree: dict = {
        '/': []
    }

    current_directory = ''

    for command in command_input:

        if command[2:] == 'cd /':
            current_directory = command[5:]
            continue

        if command[2:] == 'cd ..':
            current_directory = '/'.join(current_directory.split('/')[:-1])
            continue

        if command[2:4] == 'cd':
            current_directory = f'{current_directory}/{command[5:]}'
            continue

        if command[2:4] == 'ls':
            continue

        if command[0:3] == 'dir':

            if command[4:] not in directory_tree:
                directory_path = f'{current_directory}/{command[4:]}'
                directory_tree[directory_path] = []
            continue

        else:
            file = command.split(' ')
            directory_tree[current_directory].append({'file_name': file[1], 'file_size': int(file[0])})
            
    return directory_tree

def part_1(directory):

    total_directory_size_dict = {}

    for directory_path, contents in directory.items():

        total_directory_size = 0

        for file in contents:
            total_directory_size+=file['file_size']

        total_directory_size_dict[directory_path] = total_directory_size

    for file_directory in total_directory_size_dict:
        for file_directory_key, directory_size in total_directory_size_dict.items():
            if file_directory in file_directory_key and file_directory != file_directory_key:
                total_directory_size_dict[file_directory]+=directory_size

    return total_directory_size_dict

def part_2(total_directory_size_dict, min_space_required, total_space_available):

    directory_delete_candidates = []
    space_available = total_space_available-total_directory_size_dict['/']
    
    for directory_path, size in total_directory_size_dict.items():
        if space_available+size >= min_space_required:
            directory_delete_candidates.append({'directory': directory_path, 'file_size': size})
    
    return min(directory_delete_candidates, key=lambda directory:directory['file_size'])

if __name__ == '__main__':
    file_input = get_input()
    directory = create_directory(file_input)

    part_1_results = part_1(directory)
    part_2_results = part_2(part_1_results, 30000000, 70000000)

    print(sum([directory_size if directory_size <= 100000 else 0 for _,directory_size in part_1_results.items()]))
    print(part_2_results)
#     statement= '''
# file_input = get_input()
# part_1_results = part_1(file_input)
# part_2_results = part_2(file_input)
# '''
#     print(timeit.timeit(stmt=statement, globals=globals(), number=1000))
