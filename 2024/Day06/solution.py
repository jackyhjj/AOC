from itertools import combinations
from pathlib import Path

path = Path(__file__).parent /"input.txt"
f = open(path, "r")
maps= []
start_position = []
row = 0
col = 0
tmp = []

for line in f.readlines():
    for word in line.strip():
        if word == "^":
            start_position = [row, col]
        tmp.append(word)
        col += 1
    maps.append(tmp)
    tmp = []
    row += 1
    col = 0

f.close()

def simulate_guard(maps, start_position, extra_obstacle=None):
    """
    Simulate guard movement. Returns (visited_positions, is_loop)
    """
    row, col = start_position
    max_row = len(maps)
    max_col = len(maps[0])
    visited = set()
    visited_with_direction = set()  # Track position AND direction to detect loops
    
    # Direction: 0=up, 1=right, 2=down, 3=left
    direction = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while True:
        # Check if we've been in this exact state before (same position + direction)
        state = (row, col, direction)
        if state in visited_with_direction:
            return visited, True  # Loop detected
        
        visited_with_direction.add(state)
        visited.add((row, col))
        
        # Calculate next position
        dr, dc = directions[direction]
        next_row, next_col = row + dr, col + dc
        
        # Check if next position is out of bounds
        if next_row < 0 or next_row >= max_row or next_col < 0 or next_col >= max_col:
            return visited, False  # Guard exits the map
        
        # Check if next position is blocked
        is_blocked = (maps[next_row][next_col] == "#" or 
                     (extra_obstacle and (next_row, next_col) == extra_obstacle))
        
        if is_blocked:
            # Turn right (clockwise)
            direction = (direction + 1) % 4
        else:
            # Move forward
            row, col = next_row, next_col

def part_1(maps, start_position):
    visited, _ = simulate_guard(maps, start_position)
    return len(visited)

def part_2(maps, start_position):
    # First, get all positions the guard visits in the original path
    original_visited, _ = simulate_guard(maps, start_position)
    
    loop_count = 0
    
    # Try placing an obstacle at each position the guard originally visits
    # (except the starting position)
    for obstacle_pos in original_visited:
        if obstacle_pos == tuple(start_position):
            continue  # Can't place obstacle at starting position
        
        # Skip if there's already an obstacle here
        if maps[obstacle_pos[0]][obstacle_pos[1]] == "#":
            continue
        
        # Simulate with the new obstacle
        _, is_loop = simulate_guard(maps, start_position, obstacle_pos)
        
        if is_loop:
            loop_count += 1
    
    return loop_count

print("Part 1:", part_1(maps, start_position))
print("Part 2:", part_2(maps, start_position))