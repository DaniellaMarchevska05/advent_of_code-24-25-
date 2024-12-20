import re
from turtledemo.sorting_animate import instructions1

def XMAS_count(file_path):
    with open(file_path) as file: # 'with' helps to automatically close the file and use it as 'f'
        parts = [line.strip() for line in file.readlines()]

        rows = len(parts)
        cols = len(parts[0])
        word = 'XMAS'
        word_len = len(word)
        count = 0

        for i in range(rows):
            for j in range(cols - word_len + 1):
                if parts[i][j:j+word_len] == word:
                    count+=1
                if parts[i][j:j+word_len][::-1] == word:
                    count += 1

        for i in range(rows - word_len + 1):
            for j in range(cols):
                if "".join(parts[i+k][j] for k in range(word_len)) == word:
                    count += 1
                if "".join(parts[i + k][j] for k in range(word_len))[::-1] == word:
                    count += 1

        for i in range(rows - word_len + 1):
            for j in range(cols - word_len + 1):
                if "".join(parts[i+k][j+k] for k in range(word_len)) == word:
                    count += 1
                if "".join(parts[i+k][j+k] for k in range(word_len))[::-1] == word:
                    count += 1

        for i in range(word_len - 1, rows):
            for j in range(cols - word_len + 1):
                if "".join(parts[i-k][j+k] for k in range(word_len)) == word:
                    count += 1
                if "".join(parts[i-k][j+k] for k in range(word_len))[::-1] == word:
                    count += 1

    return count

def count_xmas(file_path):
    def check_direction(start_row, start_col, delta_row, delta_col):
        """Check for the word 'XMAS' in a specific direction."""
        count = 0
        for step in range(word_len):
            r = start_row + step * delta_row
            c = start_col + step * delta_col
            # Ensure indices are valid
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != word[step]:
                return 0
        return 1

    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    # Define the eight possible directions as (row change, col change)
    directions = [
        (0, 1),  # Horizontal (right)
        (0, -1), # Horizontal (left)
        (1, 0),  # Vertical (down)
        (-1, 0), # Vertical (up)
        (1, 1),  # Diagonal (down-right)
        (-1, -1),# Diagonal (up-left)
        (1, -1), # Diagonal (down-left)
        (-1, 1)  # Diagonal (up-right)
    ]

    for i in range(rows):
        for j in range(cols):
            for dr, dc in directions:
                count += check_direction(i, j, dr, dc)

    return count

# Example Usage
file_path = "C:\\Users\\Daniella\\PycharmProjects\\advent calendar\\nums.txt"
result = count_xmas(file_path)
print("Number of XMAS occurrences:", result)


res = XMAS_count("C:\\Users\\Daniella\\PycharmProjects\\advent calendar\\nums.txt")
print(res)
