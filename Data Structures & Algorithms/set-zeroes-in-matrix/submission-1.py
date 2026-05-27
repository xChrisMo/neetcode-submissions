from collections import deque

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # find all 0s, recursively 0 all columns and rows IF NOT 0
        directions = [[0, 1],[1, 0],[-1, 0],[0, -1]]
        zeros = deque()

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeros.append((r, c))
        
        while zeros:
            r, c = zeros.popleft()

            for nc in range(COLS):
                matrix[r][nc] = 0

            for nr in range(ROWS):
                matrix[nr][c] = 0