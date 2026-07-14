class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 by 9
        
        # each row 1-9, no duplicates
        # each col 1-9, no duplicates

        # each 3 x 3 

        # row_set = set()
        # col_set = set

        n = len(board)
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        tri_set = defaultdict(set)

        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in tri_set[(r//3, c//3)]:
                    return False

                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                tri_set[(r // 3, c // 3)].add(board[r][c])

        return True