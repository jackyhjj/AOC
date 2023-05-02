import sys, os
sys.path.insert(0, '/Volumes/Files/Projects/AOC/')

from string import ascii_lowercase, ascii_uppercase
from pathlib import Path
import re,helper, copy

dirpath = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(dirpath, 'input.txt')

input = []
crates = []
movements = []

input = helper.read_input_file(filepath, remove_space=False)

def get_crates_and_movement(input):
    no_crates = len(input[0])//4
    movement=False
    for crate in range(no_crates): crates.append([])

    for line in input:
        if (len(line.strip())) == 0:
            movement = True
            continue

        if (movement): 
            movements.append(re.findall(r'\d+', line))
        else:
            for crate in range(no_crates):
                letter = line[(crate*4)+1:((crate+1)*4)-2]
                if (letter.isalpha()):
                    crates[crate].append(letter)

def part_1():
    text = ""
    tmp_crates = copy.deepcopy(crates)
    for move in movements:
        for loop in range(int(move[0])):
            remove = tmp_crates[int(move[1])-1].pop(0)
            tmp_crates[int(move[2])-1].insert(0, remove)
    
    for crate in range(len(tmp_crates)):
        text = text + tmp_crates[crate][0]

    print(text)

def part_2():
    text = ""
    tmp_crates = copy.deepcopy(crates)
    # print(tmp_crates)

    for move in movements:
        # print(move)
        remove_stack = []
        for loop in range(int(move[0])):
            # print(loop)
            remove_stack.append(tmp_crates[int(move[1])-1].pop(0))
        
        while len(remove_stack) != 0:
            tmp_crates[int(move[2])-1].insert(0, remove_stack.pop())
        
        # print(tmp_crates)

    for crate in range(len(tmp_crates)):
        text = text + tmp_crates[crate][0]

    print(text)

get_crates_and_movement(input)
# print(crates)
# print(movements)
part_1()
part_2()