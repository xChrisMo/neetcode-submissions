class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        i = 0
        j = 0

        if len(t) > len(s): return 0
        
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if j == len(t):
                cache[(i, j)] = 1
                return cache[(i, j)]

            if i == len(s):
                cache[(i, j)] = 0
                return cache[(i, j)] 

            if s[i] != t[j]:
                cache[(i, j)] = dfs(i + 1, j)
                return cache[(i, j)]

            else:
                skip = dfs(i + 1, j)
                take = dfs(i + 1, j + 1)

                cache[(i, j)] = skip + take
                return cache[(i, j)]

        return dfs(0, 0)