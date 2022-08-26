import numpy as np

puzzle = np.array([[0, 0, 0, 0, 6, 0, 2, 4, 3],
                    [0, 2, 4, 9, 3, 0, 0, 0, 6],
                    [0, 0, 1, 4, 7, 0, 0, 0, 8],
                    [6, 0, 2, 0, 0, 9, 8, 0, 7],
                    [8, 1, 0, 2, 0, 7, 0, 3, 0],
                    [7, 0, 0, 0, 0, 6, 4, 0, 2],
                    [0, 9, 0, 5, 0, 3, 0, 0, 0],
                    [0, 0, 0, 6, 0, 1, 3, 2, 0],
                    [2, 3, 8, 0, 9, 0, 0, 0, 0]])

class SudokuSolver:
    def __init__(self, puzzle: np.ndarray):
        self.puzzle = puzzle
        self._make_rows()

    def _make_rows(self):
        for i in range(1, 10):
            setattr(self, f"self.row_{i}", self.puzzle[i-1])

puzzle_1 = SudokuSolver(puzzle)
print(puzzle_1.row_1)