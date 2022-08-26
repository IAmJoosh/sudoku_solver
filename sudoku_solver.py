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
        self._make_cols()
        self._make_boxes()

    def _make_rows(self):
        for i in range(1, 10):
            setattr(self, f"row_{i}", self.puzzle[i-1])
    
    def _make_cols(self):
        for i in range(1, 10):
            setattr(self, f"col_{i}", self.puzzle[:9, i-1:i].flatten())

    def _make_boxes(self):
        box_num = 1
        for i in range(3):
            for j in range(3):
                x1 = 3 * i
                x2 = x1 + 3
                y1 = 3 * j
                y2 = y1 + 3
            
                box = self.puzzle[x1:x2, y1:y2]
                setattr(self, f"box_{box_num}", box.flatten())
                box_num += 1

puzzle_1 = SudokuSolver(puzzle)
print(puzzle_1.row_1)
print(puzzle_1.col_1)
print(puzzle_1.box_1)