'''Coding Challenge from https://adventofcode.com/2022/day/2'''
from pathlib import Path

filepath = Path(__file__).with_name('input.txt')


'''
Part 1
ROCK: A, X
PAPER: B, Y
SCISSORS: C, Z

Part 2
LOSE: X
DRAW: Y
WIN: Z
'''

MOVE_SCORING = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

OUTCOME_SCORING = {
    'WIN': 6,
    'LOSE': 0,
    'DRAW': 3
}

ROUND_RESULTS = {
    'A X': 'DRAW',
    'A Y': 'WIN',
    'A Z': 'LOSE',
    'B X': 'LOSE',
    'B Y': 'DRAW',
    'B Z': 'WIN',
    'C X': 'WIN',
    'C Y': 'LOSE',
    'C Z': 'DRAW'
}

CHEAT_SHEET_RULES = {
    'A X': 'A Z', #LOSE
    'A Y': 'A X', #DRAW
    'A Z': 'A Y', #WIN
    'B X': 'B X', #LOSE
    'B Y': 'B Y', #DRAW
    'B Z': 'B Z', #WIN
    'C X': 'C Y', #LOSE
    'C Y': 'C Z', #DRAW
    'C Z': 'C X' #WIN
}

def get_input():
    file_input = None

    with filepath.open('r', encoding='utf-8') as file:
        file_input =  [line.rstrip('\n') for line in file]

    return file_input

def play_game_part_1(strategy_guide):
    score = 0

    for strategy in strategy_guide:
        score += (OUTCOME_SCORING[ROUND_RESULTS[strategy]] \
            + MOVE_SCORING[strategy.split(' ')[1]])

    return score

def play_game_part_2(strategy_guide):
    score = 0

    for strategy in strategy_guide:
        round_score = (OUTCOME_SCORING[ROUND_RESULTS[CHEAT_SHEET_RULES[strategy]]] \
            + MOVE_SCORING[CHEAT_SHEET_RULES[strategy].split(' ')[1]])

        score += round_score

    return score

if __name__ == "__main__":
    file_input = get_input()
    part_1_outcome = play_game_part_1(file_input)
    part_2_outcome = play_game_part_2(file_input)

    print(part_1_outcome)
    print(part_2_outcome)