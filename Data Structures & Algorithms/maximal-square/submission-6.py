class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]

            if r >= ROWS or c >= COLS:
                cache[(r, c)] = 0
                return cache[(r, c)]

            if matrix[r][c] == '1':
                cache[(r, c)] = 1 + min(
                    dfs(r, c + 1),
                    dfs(r + 1, c + 1),
                    dfs(r + 1, c),
                )

            else:
                cache[(r, c)] = 0

            return cache[(r, c)]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)

        return max(cache.values()) ** 2