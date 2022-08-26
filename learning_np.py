import numpy as np

# Testing puzzle from https://www.nytimes.com/puzzles/sudoku/easy August 26th 2022
puzzle = np.array([[0, 0, 0, 0, 6, 0, 2, 4, 3],
                    [0, 2, 4, 9, 3, 0, 0, 0, 6],
                    [0, 0, 1, 4, 7, 0, 0, 0, 8],
                    [6, 0, 2, 0, 0, 9, 8, 0, 7],
                    [8, 1, 0, 2, 0, 7, 0, 3, 0],
                    [7, 0, 0, 0, 0, 6, 4, 0, 2],
                    [0, 9, 0, 5, 0, 3, 0, 0, 0],
                    [0, 0, 0, 6, 0, 1, 3, 2, 0],
                    [2, 3, 8, 0, 9, 0, 0, 0, 0]])

# print(puzzle)
# print(puzzle.ndim)
# print(puzzle.size)

test_row = 0
test_col = 4
complete = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # row first then column for indexing
# # index using comma instead of 2 pairs of square brackets
# print(puzzle[test_row, test_col])

# printing 5th column: index=4
# print(np.array(puzzle[:9, test_col:test_col+1]).flatten())

for row_index, row in enumerate(puzzle, start=1):
    for col, cell in enumerate(row, start=1):
        if cell != 0:
            pass

        else:
            column = puzzle[:9, col-1:col].flatten()
            look_row_and_col = np.union1d(row, column)
            candidates = np.setdiff1d(complete, look_row_and_col)
            if len(candidates) == 2:
                print(f"Row {row_index}: {row}")
                print(f"Column {col}: {column}")
                print(f"Candidates: {candidates}")