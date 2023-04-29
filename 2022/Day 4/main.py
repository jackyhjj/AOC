import sys, os
sys.path.insert(0, '/Volumes/Files/Projects/AOC/')

from string import ascii_lowercase, ascii_uppercase
from pathlib import Path
import re
import helper

dirpath = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(dirpath, 'input.txt')

input = []

input = helper.read_input_file(filepath)

def split_numbers(line):
    test = line.split(',')
    start_a, end_a= map(int, test[0].split('-'))
    start_b, end_b= map(int, test[1].split('-'))

    return start_a, end_a, start_b, end_b



def part_1(input):
    total_count = 0
    for line in input:
        start_a, end_a, start_b, end_b = split_numbers(line)
        
        if (start_a >= start_b and end_a <= end_b) or \
            (start_b >= start_a and end_b <= end_a):
            total_count += 1

    return total_count

def part_2(input):
    total_count = 0
    for line in input:
        start_a, end_a, start_b, end_b = split_numbers(line)

        if (start_a >= start_b and start_a <= end_b)or \
            (start_b >= start_a and start_b <= end_a) :
            total_count += 1

    return total_count

print(part_1(input))
print(part_2(input))