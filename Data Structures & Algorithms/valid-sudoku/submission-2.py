class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue 

                elif val in row_set[r] or val in col_set[c] or val in square_set[(r // 3, c // 3)]:
                    return False

                row_set[r].add(val)
                col_set[c].add(val)
                square_set[(r // 3, c // 3)].add(val)

        return True