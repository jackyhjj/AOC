import sys
import os

# Add the root directory to Python path to import helper
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from helper import read_lines, read_as_integers, read_grid

file = 'sample.txt'

# Example usage of helper functions:
# Test reading integers
if os.path.exists(file):
    numbers = read_lines(file)
    print(f"Numbers from file: {numbers}")

# For your actual solutions, use:
# data = read_lines('input.txt')  # Read all lines
# numbers = read_as_integers('input.txt')  # Read as integers
# grid = read_grid('input.txt')  # Read as 2D grid
