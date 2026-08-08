class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i == n:
                cache[i] = 1
                return cache[i] 

            if s[i] == '0':
                cache[i] = 0
                return cache[i]

            cache[i] = dfs(i + 1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                cache[i] += dfs(i + 2)

            return cache[i]

        return dfs(0)
