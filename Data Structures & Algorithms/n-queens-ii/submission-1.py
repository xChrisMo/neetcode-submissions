class Solution:
    def totalNQueens(self, n: int) -> int:
        pos_diag = set()
        neg_diag = set()
        col = set()
        out = [['.'] * n for i in range(n)] 
        res = 0

        def backtrack(r):
            nonlocal res
            # base condition
            if r == n:
                res += 1
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                out[r][c] = 'Q'
                
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

                out[r][c] = '.'

        backtrack(0)
        return res