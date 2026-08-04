class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # get the count of row, count of column
        # 3 rows, 2 cols

        # it now becomes 2 rows, 3 cols

        # iterate from right to left on each row, making it the column, mkae right to mean down?

        l = 0
        r = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix)
        ROWS = len(matrix)
        COLS = len(matrix[0])

        out = [[0] * (ROWS) for i in range(COLS)]
        
        
        for r in range(ROWS):
            for c in range(COLS):
                out[c][r] = matrix[r][c]

        return out
