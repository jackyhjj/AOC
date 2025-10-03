import re
from pathlib import Path

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
pattern_until_first_dont = r'.*?(?=don\'t\(\))'
mul_str = ""

def star_1(line: str) -> int:
    results = re.finditer(pattern, line)
    final_result = 0;
    for mul in results:
        num1, num2 = mul.groups() 
        final_result += int(num1) * int(num2)
    return final_result

def star_2(line: str) -> int:
        # Regex pattern to find mul() instructions
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    # Regex pattern to find do() and don't() instructions
    control_pattern = re.compile(r"do\(\)|don't\(\)")
    
    # Splitting the string on mul() and control commands while keeping delimiters
    tokens = re.split(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', line)
    
    # Initial state: mul instructions are enabled
    mul_enabled = True
    total = 0
    
    for token in tokens:
        if not token or token.isspace():
            continue
        
        if token == "do()":
            mul_enabled = True
        elif token == "don't()":
            mul_enabled = False
        else:
            match = mul_pattern.match(token)
            if match and mul_enabled:
                num1, num2 = map(int, match.groups())
                total += num1 * num2
    
    return total

path = Path(__file__).parent / "sample_input2.txt"
f = open(path, "r")

for line in f.readlines():
    mul_str = mul_str + line
f.close()


print(star_2(mul_str))






        
