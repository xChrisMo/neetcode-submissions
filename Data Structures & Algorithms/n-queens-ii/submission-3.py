class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0

        row_set = set()
        neg_diag_set = set()
        pos_diag_set = set()
        board = [['.'] * n for _ in range(n)]

        def dfs(c):
            if c == n:
                self.res += 1
                return 

            for r in range(n):
                if r not in row_set and (r + c) not in pos_diag_set and (r - c) not in neg_diag_set:
                    board[r][c] = 'Q'
                    row_set.add(r)
                    pos_diag_set.add(r + c)
                    neg_diag_set.add(r - c)
                    # recurse
                    dfs(c + 1)

                    # backtrack
                    board[r][c] = '.'
                    row_set.remove(r)
                    pos_diag_set.remove(r + c)
                    neg_diag_set.remove(r - c)

        dfs(0)
        return self.res


                    