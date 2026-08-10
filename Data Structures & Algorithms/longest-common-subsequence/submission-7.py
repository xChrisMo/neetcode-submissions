class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # i at its end
            if i == m:
                cache[(i, j)] = 0
                return cache[(i, j)]

            # j at its end
            if j == n:
                cache[(i, j)] = 0
                return cache[(i, j)]
            
            # good match
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)
                return cache[(i, j)]

            # total mistmatch
            if text1[i] != text2[j]:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
                return cache[(i, j)]

        return dfs(0, 0)