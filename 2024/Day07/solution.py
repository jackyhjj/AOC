from itertools import product
from pathlib import Path

path = Path(__file__).parent / "input.txt"
result_list = []
number_list = []

f = open(path, "r")
for line in f.readlines():
    line = line.strip()
    if line:
        tmp = line.split(":")
        result_list.append(int(tmp[0].strip()))
        
        numbers = []
        for num in tmp[1].strip().split(" "):
            numbers.append(int(num.strip()))
        number_list.append(numbers)
f.close()

def get_operator_combinations(num_operators, include_concat=False):
    if include_concat:
        operators = ['+', '*', '||']
    else:
        operators = ['+', '*']
    return list(product(operators, repeat=num_operators))

def evaluate_expression(numbers, operators):
    """Evaluate left-to-right without operator precedence"""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            # Concatenation: join the numbers as strings, then convert back to int
            result = int(str(result) + str(numbers[i + 1]))
    return result

def part_1():
    final_result_list = []
    
    for i in range(len(result_list)):
        target = result_list[i]
        numbers = number_list[i]
        
        # Need (len(numbers) - 1) operators
        num_operators_needed = len(numbers) - 1
        if num_operators_needed == 0:
            if numbers[0] == target:
                final_result_list.append(target)
            continue
            
        operator_combinations = get_operator_combinations(num_operators_needed, include_concat=False)
        
        found = False
        for operators in operator_combinations:
            result_value = evaluate_expression(numbers, operators)
            if result_value == target:
                final_result_list.append(target)
                print(f"Found: {numbers} with {operators} = {target}")
                found = True
                break
        
        if not found:
            print(f"No solution for {target} with {numbers}")
    
    return sum(final_result_list)

def part_2():
    final_result_list = []
    
    for i in range(len(result_list)):
        target = result_list[i]
        numbers = number_list[i]
        
        # Need (len(numbers) - 1) operators
        num_operators_needed = len(numbers) - 1
        if num_operators_needed == 0:
            if numbers[0] == target:
                final_result_list.append(target)
            continue
            
        operator_combinations = get_operator_combinations(num_operators_needed, include_concat=True)
        
        found = False
        for operators in operator_combinations:
            result_value = evaluate_expression(numbers, operators)
            if result_value == target:
                final_result_list.append(target)
                print(f"Found: {numbers} with {operators} = {target}")
                found = True
                break
        
        if not found:
            print(f"No solution for {target} with {numbers}")
    
    return sum(final_result_list)

print("Part 1:", part_1())
print("Part 2:", part_2())