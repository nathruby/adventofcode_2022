'''Coding Challenge from https://adventofcode.com/2022/day/1'''

def get_input():
    input = []

    with open('input.txt', 'r', encoding='utf-8') as file:
        input =  [int(line) if line[:-1].isdigit() else '' for line in file]
   
    return input

def organize_grocery_list(grocery_list):
    organized_list = []
    calorie_count = 0

    for item in grocery_list:
        if item == '':
            organized_list.append(calorie_count)
            calorie_count = 0
        else:
            calorie_count+=item

    if calorie_count != 0:
        organized_list.append(calorie_count)

    return organized_list

if __name__ == "__main__":

    file_input = get_input()
    organized_grocery_list = organize_grocery_list(file_input)

    #part 1. Find the largest calorie consumer
    print(max(organized_grocery_list))

    #part 2. Sum of 3 largest calorie consumers
    print(sum(sorted(organized_grocery_list, reverse=True)[:3]))
