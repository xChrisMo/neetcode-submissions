class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache = {}
        # def dfs(r, c):
        #     if (r, c) in cache:
        #         return cache[(r, c)]
        #     # got to end
        #     if r == m - 1 and c == n - 1:
        #         cache[(r, c)] = 1
        #         return cache[(r, c)]

        #     if r >= m:
        #         cache[(r, c)] = 0
        #         return cache[(r, c)]

        #     if c >= n:
        #         cache[(r, c)] = 0
        #         return cache[(r, c)]

        #     cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return cache[(r, c)]

        # return dfs(0, 0)

        # dp = [[0] * n for _ in range(m)]
        # dp[m - 1][n - 1] = 1
        # for r in range(m):
        #     dp[r][n - 1] = 1
        # for c in range(n):
        #     dp[m - 1][c] = 1

        # for r in range(m - 2, -1, -1):
        #     for c in range(n - 2, -1, -1):
        #         dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

        # return dp[0][0]

        dp = [1] * n
        print(dp)
        

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[c] += dp[c + 1] # going right

        return dp[0]