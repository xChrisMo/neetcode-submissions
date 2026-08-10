class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # cache = {}

        # def dfs(i, j):
        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     # i at its end
        #     if i == m:
        #         cache[(i, j)] = 0
        #         return cache[(i, j)]

        #     # j at its end
        #     if j == n:
        #         cache[(i, j)] = 0
        #         return cache[(i, j)]
            
        #     # good match
        #     if text1[i] == text2[j]:
        #         cache[(i, j)] = 1 + dfs(i + 1, j + 1)
        #         return cache[(i, j)]

        #     # total mistmatch
        #     if text1[i] != text2[j]:
        #         cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
        #         return cache[(i, j)]

        # return dfs(0, 0)

        # dp = [[0] * n for _ in range(m)]

        # for r in range(m - 1, -1, -1):
        #     for c in range(n - 1, - 1, -1):
        #         right = dp[r][c + 1] if c + 1 < n else 0
        #         down = dp[r + 1][c] if r + 1 < m else 0
        #         diagonal = dp[r + 1][c + 1] if r + 1 < m and c + 1 < n else 0

        #         if text1[r] == text2[c]:
        #             dp[r][c] = 1 + diagonal

        #         else:
        #             dp[r][c] = max(right, down)

        # return dp[0][0]

        dp = [0] * (n + 1)

        for r in range(m - 1, -1, -1):
            prev_diag = 0
            for c in range(n - 1, -1, -1):
                old_down = dp[c]

                if text1[r] == text2[c]:
                    dp[c] = 1 + prev_diag

                else:
                    dp[c] = max(dp[c], dp[c + 1])
                    #           down and right

                prev_diag = old_down
        return dp[0]