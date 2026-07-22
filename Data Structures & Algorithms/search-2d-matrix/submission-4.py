class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we knwo each row is sorted, 
        # condition, if value


        # get number of rows
        # get number of columns
        # get middle point of rows, # middle poiny of columns
        # if that is left than target, l = m + 1
        # else, r = m! 
        
        # condition. if matrix[r][c] > target: return True
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def condition(m):
            return matrix[m // COLS][m % COLS] >= target

        l = 0
        r = (ROWS * COLS) - 1

        while l < r:
            m = l + (r - l) // 2

            # how could I have split it all into two halves

            if condition(m):
                r = m

            else:
                l = m + 1

        
        if matrix[l // COLS][l % COLS] == target: 
            return True
        return False


        # rows = 3
        # cols = 4

        # 