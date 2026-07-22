class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we knwo each row is sorted, 
        # condition, if value


        # get number of rows
        # get number of columns
        # get middle point of rows, # middle poiny of columns
        # if that is left than target, l = m + 1
        # else, r = m! 

        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = (ROWS * COLS) - 1

        while l <= r:
            m = l + (r - l) // 2

            # how could I have split it all into two halves

            row = m // COLS
            col = m % COLS

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                l = m + 1

            else:
                r = m - 1

        return False


        # rows = 3
        # cols = 4

        # 