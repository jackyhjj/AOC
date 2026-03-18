import sys
import os

# Add the root directory to Python path to import helper
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from helper import read_lines, read_as_integers, read_grid

import hashlib


def find_advent_coin(secret_key, prefix="000000", show_progress=True):
    number = 1
    while True:
        hash_result = hashlib.md5(f"{secret_key}{number}".encode()).hexdigest()

        if hash_result.startswith(prefix):
            return number

        if show_progress and number % 100000 == 0:
            print(f"Checked {number:,} numbers...")

        number += 1


# Usage
secret_key = "abcdef"
secret_key = "bgvyzdsv"
result = find_advent_coin(secret_key, show_progress=True)
print(f"\nAnswer: {result}")