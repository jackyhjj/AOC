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

# keep backups so a --limit quick-run can slice them later without re-reading the file
original_result_list = result_list.copy()
original_number_list = [nums.copy() for nums in number_list]

def solve_target(numbers, target, include_concat=False):
    """
    DFS left-to-right search that chooses operators between numbers to reach target.

    State: (idx, current_value) where idx is the index of the next number to consume
    (numbers[idx]). Start: idx=1, current_value=numbers[0].

    Optimizations used:
    - Prune when current_value > target because all numbers are positive and operators
      ('+', '*', '||') never decrease the value.
    - Memoize failing states (idx, current_value) -> False to avoid re-searching same subtrees.

    Returns True if a valid operator sequence exists, otherwise False.
    """
    from functools import lru_cache

    n = len(numbers)

    # quick checks
    if n == 0:
        return False
    if n == 1:
        return numbers[0] == target

    # Use recursion with memo
    seen = {}

    def dfs(idx, cur):
        # idx is index of next number to incorporate (1..n-1)
        if idx == n:
            return cur == target

        key = (idx, cur)
        if key in seen:
            return False

        # pruning: if cur already greater than target, we cannot reduce (numbers positive)
        if cur > target:
            seen[key] = False
            return False

        nxt = numbers[idx]

        # Try '+'
        if dfs(idx + 1, cur + nxt):
            return True

        # Try '*'
        # Multiplication may blow up quickly; check before recursing to avoid overflow-ish growth
        if dfs(idx + 1, cur * nxt):
            return True

        # Try concatenation if allowed: concat current value and next number as strings
        if include_concat:
            try:
                concat_val = int(str(cur) + str(nxt))
            except Exception:
                concat_val = cur * (10 ** (len(str(nxt)))) + nxt
            if dfs(idx + 1, concat_val):
                return True

        seen[key] = False
        return False

    return dfs(1, numbers[0])

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
            
        # Use optimized DFS search without concatenation
        found = solve_target(numbers, target, include_concat=False)
        if found:
            final_result_list.append(target)
            print(f"Found: {numbers} = {target}")
        else:
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
            
        # Use optimized DFS search with concatenation allowed
        found = solve_target(numbers, target, include_concat=True)
        if found:
            final_result_list.append(target)
            print(f"Found: {numbers} = {target}")
        else:
            print(f"No solution for {target} with {numbers}")
    
    return sum(final_result_list)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run Day07 solution parts")
    parser.add_argument("--part", choices=["1", "2", "all"], default="all",
                        help="Which part to run (default: all)")
    parser.add_argument("--limit", type=int, default=None,
                        help="If set, only use the first N input lines (quick test)")
    args = parser.parse_args()

    # restore full lists then optionally slice for quick tests
    result_list[:] = original_result_list
    number_list[:] = original_number_list
    if args.limit is not None:
        result_list = result_list[: args.limit]
        number_list = number_list[: args.limit]

    if args.part in ("1", "all"):
        print("Part 1:", part_1())
    if args.part in ("2", "all"):
        print("Part 2:", part_2())