# CHECK FOR 3 VOWELS
import sys
import os
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from helper import read_lines, read_as_integers, read_grid


def has_enough_vowels(s : str)-> bool:
    return sum( 1 for c in s if c in 'aeiou' ) >= 3

# CHECK FOR DOUBLE LETTER
def has_double_letters(s : str)-> bool:
    return any(s[i] == s[i+1] for i in range(len(s)-1))

# CHECK FOR ANY ILLEGAL CHARS
def has_no_illegal_chars(s : str)-> bool:
    return re.search('ab|cd|pq|xy', s) is None

# HAS 2 DOUBLE LETTERS NOT OVERLAPPING
def has_double_letter_no_overlapping(s : str)-> bool:
    for i in range(len(s)-1):
        pair = s[i:i+2]
        if pair in s[i+2:]:
            return True
    return False

# HAS REPEATED LETTER WITH DIFFERENT LETTER IN BETWEEN
def has_repeated_with_one_letter_space(s : str)-> bool:
    return any(s[i] == s[i+2] for i in range(len(s)-2))

def classify_part1(s: str) -> str:
    failures = []
    if not has_enough_vowels(s):
        failures.append("less than 3 vowels")
    if not has_double_letters(s):
        failures.append("no double letter")
    if not has_no_illegal_chars(s):
        failures.append("contains a forbidden pair (ab/cd/pq/xy)")
    return "nice" if not failures else f"naughty ({'; '.join(failures)})"

def classify_part2(s: str) -> str:
    failures = []
    if not has_double_letter_no_overlapping(s):
        failures.append("No double letters")
    if not has_repeated_with_one_letter_space(s):
        failures.append("No repeated with one letter space")
    return "nice" if not failures else f"naughty ({'; '.join(failures)})"

def print_results(strings: list) -> None:

    print(f"Part 1")
    print(f"=============")
    nice_count = 0
    for s in strings:
        result = classify_part1(s)
        icon = "🎁" if result == "nice" else "💀"
        print(f"{icon}  {s!r:42s} -> {result}")
        if result == "nice":
            nice_count += 1
    print(f"\n{'─' * 64}")
    print(f"Total strings : {len(strings)}")
    print(f"Nice          : {nice_count}")
    print(f"Naughty       : {len(strings) - nice_count}")

    print(f"Part 2")
    print(f"=============")
    nice_count = 0
    for s in strings:
        result = classify_part2(s)
        icon = "🎁" if result == "nice" else "💀"
        print(f"{icon}  {s!r:42s} -> {result}")
        if result == "nice":
            nice_count += 1
    print(f"\n{'─' * 64}")
    print(f"Total strings : {len(strings)}")
    print(f"Nice          : {nice_count}")
    print(f"Naughty       : {len(strings) - nice_count}")

file = 'input.txt'

# Example usage of helper functions:
# Test reading integers
if os.path.exists(file):
    numbers = read_lines(file)
    print(f"Numbers from file: {numbers}")

    EXAMPLES = [
        "ugknbfddgicrmopn",
        "aaa",
        "jchzalrnumimnmhp",
        "haegwjzuvuyypxyu",
        "dvszwmarrgswjxmb",
    ]

    print(f"Examples\n")
    print("===============\n")
    print_results(EXAMPLES)

    print(f"Real Puzzle\n")
    print("===============\n")
    print_results(numbers)