from pathlib import Path

path = Path(__file__).parent / "input.txt"
f = open(path, "r")
safe_counter = 0
levels = []

def is_safe(report):
    increasing = all(report[i] < report[i+1] and 1 <= report[i+1] - report[i] <= 3 for i in range(len(report)-1))
    decreasing = all(report[i] > report[i+1] and 1 <= report[i] - report[i+1] <= 3 for i in range(len(report)-1))
    return increasing or decreasing

def can_be_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

for line in f.readlines():
    levels.append([int(s) for s in line.split()])
f.close()

safe_count = sum(is_safe(level) for level in levels)
print(f"Number of safe reports: {safe_count}")
safe_count = sum(is_safe(level) or can_be_safe_with_dampener(level) for level in levels)
print(f"Number of safe dampened reports: {safe_count}")

print(levels[0])
print(levels[0][:2] + levels[0][3:])
