'''Coding Challenge from https://adventofcode.com/2022/day/7'''
from pathlib import Path
import timeit

filepath = Path(__file__).with_name('input.txt')

class Directory():

    name: str
    parent: str
    directories: dict
    files: dict
    total_size: int

    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.directories = {}
        self.files = {}
        self.total_size = None

    def add_dir(self, name):
        self.directories[name] = Directory(name,self)

    def add_file(self, name, size):
        self.files[name] = size

    def size(self):
        if self.total_size is None:
            self.total_size = sum(self.files.values()) \
                + sum( [directory.size() for directory in self.directories.values()] )

        return self.total_size

    def __str__(self) -> str:
        return f'Name: {self.name}, Size: {self.size()}'

def get_input():

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input

def create_directory(command_input):

    root: Directory = Directory('/', None)

    current_directory: Directory = root

    for command in command_input:

        if command == '$ cd /':
            current_directory = root
            continue

        if command == '$ cd ..':
            current_directory = current_directory.parent
            continue

        if command[2:4] == 'cd':
            current_directory = current_directory.directories[command[5:]]
            continue

        if command == '$ ls':
            continue

        if command.startswith('dir'):

            current_directory.add_dir(command[4:])
            continue

        else:
            file = command.split( )
            current_directory.add_file(file[1], int(file[0]))

    return root

def part_1(root: Directory, max_file_size: int):

    directory_path: list[Directory] = [root]
    total: int = 0

    while len(directory_path) > 0:
        current_directory: Directory = directory_path[0]

        if current_directory.size() <= max_file_size:
            total += current_directory.size()

        directory_path.extend(current_directory.directories.values())

        directory_path = directory_path[1:]

    return total

def part_2(root: Directory, min_space_required: int, total_space_available: int):

    directory_path: list[Directory] = [root]
    space_available: int = total_space_available-root.size()
    delete_candidates: list[Directory] = []

    while len(directory_path) > 0:
        current_directory: Directory = directory_path[0]

        if space_available+current_directory.size() >= min_space_required:
            delete_candidates.append(current_directory)

        directory_path.extend(current_directory.directories.values())

        directory_path = directory_path[1:]

    return min(delete_candidates, key=lambda directory:directory.size())

if __name__ == '__main__':
    file_input = get_input()
    directory_root = create_directory(file_input)

    part_1_results = part_1(directory_root, 100*1000)
    part_2_results = part_2(directory_root, 30*1000*1000, 70*1000*1000)

    print(part_1_results)
    print(part_2_results)

#     statement= '''
# file_input = get_input()
# directory_root = create_directory(file_input)

# part_1_results = part_1(directory_root, 100*1000)
# part_2_results = part_2(directory_root, 30*1000*1000, 70*1000*1000)
# '''
#     print(timeit.timeit(stmt=statement, globals=globals(), number=1000))
