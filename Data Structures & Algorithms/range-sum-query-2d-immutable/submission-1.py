class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # every position, it is the sum of every other row + column before it
        # we would have to loop throught every position totally
        # we reproduce the range from scratch, but pad the edges if anything! this is a guard for the off by one errors!
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.square = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            preSum = 0
            for c in range(COLS):
                preSum += matrix[r][c]
                above = self.square[r][c + 1] # row before, but same column! 
                self.square[r + 1][c + 1] = above + preSum    


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # to get the sum of a submatrix, we 
        # bottomright - above - left + topLeft
        # we do this because the sum at each position is more than  jsut a small box, it is everything we have seen so far..
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1

        bottomright = self.square[row2][col2] # rows in matrix is square + 1!
        above = self.square[row1 - 1][col2]
        left = self.square[row2][col1 - 1]
        current = self.square[row2][col2]
        topLeft = self.square[row1 - 1][col1 - 1]

        sumsum = bottomright - left - above + topLeft 
        return sumsum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)