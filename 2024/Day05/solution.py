from itertools import combinations
from pathlib import Path

path = Path(__file__).parent /"input.txt"
f = open(path, "r")
lines = []

rules = []
start_question = False
questions = []

for line in f.readlines():
    if line.strip() == "":
        start_question = True
        continue

    if start_question:
        questions.append(line.strip())
    else:
        rules.append(list(line.strip().split("|")))

f.close()

def part_1(rules, questions):
    count = 0
    for question in questions:
        digits = question.split(",")
        pairs = [list(p) for p in combinations(digits, 2)]
        is_subset = all(x in rules for x in pairs)
        idx = len(digits) // 2
        if is_subset:
            print(digits[idx])
            count += int(digits[idx])
    return count

def parse_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')
    
    # Find the blank line that separates rules from updates
    blank_line = lines.index('')
    
    # Parse rules: "47|53" -> (47, 53)
    rules = []
    for line in lines[:blank_line]:
        a, b = line.split('|')
        rules.append((int(a), int(b)))
    
    # Parse updates: "75,47,61,53,29" -> [75, 47, 61, 53, 29]
    updates = []
    for line in lines[blank_line + 1:]:
        update = [int(x) for x in line.split(',')]
        updates.append(update)
    
    return rules, updates


def is_correct_order(update, rules):
    # Check if this update follows all the rules
    for a, b in rules:
        # Only check rules that apply to pages in this update
        if a in update and b in update:
            pos_a = update.index(a)
            pos_b = update.index(b)
            if pos_a > pos_b:  # a should come before b
                return False
    return True


def fix_order(update, rules):
    # Keep swapping until it's correct
    fixed = update.copy()
    
    while not is_correct_order(fixed, rules):
        # Find a rule that's broken and fix it
        for a, b in rules:
            if a in fixed and b in fixed:
                pos_a = fixed.index(a)
                pos_b = fixed.index(b)
                if pos_a > pos_b:  # Wrong order! Swap them
                    fixed[pos_a], fixed[pos_b] = fixed[pos_b], fixed[pos_a]
                    break  # Check all rules again from the start
    
    return fixed


def get_middle(lst):
    return lst[len(lst) // 2]


def solve():
    rules, updates = parse_input(path)
    
    total = 0
    for update in updates:
        if not is_correct_order(update, rules):
            # This update is wrong, fix it
            fixed_update = fix_order(update, rules)
            middle = get_middle(fixed_update)
            total += middle
            print(f"Fixed {update} -> {fixed_update}, middle = {middle}")
    
    return total

print("Part 1:", part_1(rules, questions))
print("Part 2:", solve())
