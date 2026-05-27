from collections import deque

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # find all 0s, recursively 0 all columns and rows IF NOT 0
        ROWS = len(matrix)
        COLS = len(matrix[0])

        seen_row = set()
        seen_col = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    seen_row.add(r)
                    seen_col.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in seen_row or c in seen_col:
                    matrix[r][c] = 0
