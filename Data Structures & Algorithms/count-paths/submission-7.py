class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            # got to end
            if r == m - 1 and c == n - 1:
                cache[(r, c)] = 1
                return cache[(r, c)]

            if r < 0 or r >= m:
                cache[(r, c)] = 0
                return cache[(r, c)]

            if c < 0 or c >= n:
                cache[(r, c)] = 0
                return cache[(r, c)]

            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]

        return dfs(0, 0)