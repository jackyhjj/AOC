from pathlib import Path

path = Path(__file__).parent / "input.txt"
f = open(path, "r")
lines = []

for line in f.readlines():
    lines.append(list(line.strip()))
f.close()

def count_xmas_word(string_matrix):
    count = 0
    rows = len(string_matrix)
    cols = len(string_matrix[0])
    target = "XMAS"
    
    # All 8 directions: right, left, down, up, down-right, down-left, up-right, up-left
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                # Check if we can fit the word in this direction
                end_x, end_y = i + dx * 3, j + dy * 3
                if 0 <= end_x < rows and 0 <= end_y < cols:
                    # Check if the word matches
                    word = ""
                    for k in range(4):
                        word += string_matrix[i + dx * k][j + dy * k]
                    if word == target:
                        count += 1
    return count

def count_x_mas(string_matrix):
    count = 0
    rows = len(string_matrix)
    cols = len(string_matrix[0])
    
    # Check each possible center position for an X-MAS
    for i in range(1, rows - 1):  # Can't be on edges
        for j in range(1, cols - 1):  # Can't be on edges
            if string_matrix[i][j] == 'A':  # Center must be 'A'
                # Check the two diagonals
                # Top-left to bottom-right diagonal
                diag1 = string_matrix[i-1][j-1] + string_matrix[i][j] + string_matrix[i+1][j+1]
                # Top-right to bottom-left diagonal  
                diag2 = string_matrix[i-1][j+1] + string_matrix[i][j] + string_matrix[i+1][j-1]
                
                # Both diagonals must be "MAS" or "SAM"
                if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                    count += 1
    
    return count


result = count_xmas_word(lines)
print(result)
result = count_x_mas(lines)
print(result)