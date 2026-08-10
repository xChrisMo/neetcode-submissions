class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        cache = {}
        def dfs(r, c):
            # from 0, 0 to m - 1, n - 1
            # at every point we check the minimum between right and down
            # the issue is the summing... give hints on this for my base recursion ?
            if (r, c) in cache:
                return cache[(r, c)]

            if r == ROWS or c == COLS:
                cache[(r, c)] = float('inf')
                return cache[(r, c)]

            if r == ROWS - 1 and c == COLS - 1:
                cache[(r, c)] = grid[r][c]
                return cache[(r, c)]
                
            cache[(r, c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return cache[(r, c)]

        return dfs(0, 0)
