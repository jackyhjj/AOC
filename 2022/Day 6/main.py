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

def part_1():
    counter = 0
    curr_text = ""
    curr_text = input[0][counter:counter+4]
    while(len(set(curr_text)) != 4):
        counter+=1
        curr_text = input[0][counter:counter+4]
    
    print(counter+4)

def part_2():
    counter = 0
    curr_text = ""
    curr_text = input[0][counter:counter+14]
    print(curr_text)
    while(len(set(curr_text)) != 14):
        counter+=1
        curr_text = input[0][counter:counter+14]
        print(curr_text)
    
    print(counter+14)

part_1()
part_2()