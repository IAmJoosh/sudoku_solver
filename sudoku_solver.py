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

    complete = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

    def solve_using_sight(self):
        for row_index, row in enumerate(self.puzzle, start=1):
            for col_index, cell in enumerate(row, start=1):
                
                if cell != 0:
                    pass

                else:
                    can_see_no_box = np.union1d(getattr(self, f"row_{row_index}"), getattr(self, f"col_{col_index}"))

                    if row_index < 4:
                        if col_index < 4:
                            box_num = 1
                        elif col_index < 7:
                            box_num = 2
                        elif col_index < 10:
                            box_num = 3
                    
                    elif row_index < 7:
                        if col_index < 4:
                            box_num = 4
                        elif col_index < 7:
                            box_num = 5
                        elif col_index < 10:
                            box_num = 6
                    
                    elif row_index < 10:
                        if col_index < 4:
                            box_num = 7
                        elif col_index < 7:
                            box_num = 8
                        elif col_index < 10:
                            box_num = 9

                    can_see = np.union1d(can_see_no_box, getattr(self, f"box_{box_num}"))
                    candidates = np.setdiff1d(SudokuSolver.complete, can_see)
                    # print(f"Row Num: {row_index}")
                    # print(f"Column Num: {col_index}")
                    # print(f"Candidates: {candidates}")
                    # print(f"Box Number: {box_num}")

puzzle_1 = SudokuSolver(puzzle)
# print(puzzle_1.row_1)
# print(puzzle_1.col_1)
# print(puzzle_1.box_1)

puzzle_1.solve_using_sight()