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

print(puzzle)
print(puzzle.ndim)
print(puzzle.size)