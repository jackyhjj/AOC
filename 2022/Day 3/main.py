import sys, os
sys.path.insert(0, '/Volumes/Files/Projects/AOC/')

from string import ascii_lowercase, ascii_uppercase
from pathlib import Path
import helper

dirpath = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(dirpath, 'input.txt')

input = []

def part_1():
    total = 0
    for line in input:
        counter = len(line)
        # print(line)

        compartment_1 = line[:int((counter / 2))]
        compartment_2 = line[int(counter / 2):]

        same_item_list = set(compartment_1).intersection(compartment_2)

        for item in same_item_list:
            if item in ascii_lowercase:
                total += ascii_lowercase.index(item) + 1
            else:
                total += ascii_uppercase.index(item) + 27

    return total

def part_2():
    rucksack_lists = []
    total = 0
    for line in input:
        rucksack_lists.append(line)
        
        if len(rucksack_lists) == 3:
            first_bag = set(rucksack_lists[0])
            second_bag = set(rucksack_lists[1])
            third_bag = set(rucksack_lists[2])
            same_item_list = list((first_bag.intersection(second_bag)).intersection(third_bag))
            # print(same_item_list)

            if same_item_list[0] in ascii_lowercase:
                total += ord(same_item_list[0]) - ord('a') + 1
            else:
                total += ord(same_item_list[0]) - ord('A') + 27
            
            rucksack_lists = []

    return total

input = helper.read_input_file(filepath)

print(part_1())
print(part_2())
