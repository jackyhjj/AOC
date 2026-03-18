import sys
import os

# Add the root directory to Python path to import helper
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from helper import read_lines, read_as_integers, read_grid

file = 'input.txt'

# Example usage of helper functions:
# Test reading integers
if os.path.exists(file):
    numbers = read_lines(file)
    print(f"Numbers from file: {numbers[0]}")
    x = 0
    x2 = 0
    y = 0
    y2 = 0
    visited = []

    visited.append((x,y))
    for index,direction in enumerate(numbers[0]):
        if index%2 == 0:
            if direction == '^':
                y += 1
            elif direction == 'v':
                y -= 1
            elif direction == '<':
                x -= 1
            elif direction == '>':
                x += 1
            visited.append((x,y))
        else:
            if direction == '^':
                y2 += 1
            elif direction == 'v':
                y2 -= 1
            elif direction == '<':
                x2 -= 1
            elif direction == '>':
                x2 += 1

            visited.append((x2, y2))

    print(len(list(set(visited))))


# For your actual solutions, use:
# data = read_lines('input.txt')  # Read all lines
# numbers = read_as_integers('input.txt')  # Read as integers
# grid = read_grid('input.txt')  # Read as 2D grid
