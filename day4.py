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

res = XMAS_count("C:\\Users\\Daniella\\PycharmProjects\\advent calendar\\nums.txt")
print(res)
