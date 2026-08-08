class Solution:
    def numDecodings(self, s: str) -> int:
        # n = len(s)
        # cache = {}

        # def dfs(i):
        #     if i in cache:
        #         return cache[i]

        #     if i == n:
        #         cache[i] = 1
        #         return cache[i] 

        #     if s[i] == '0':
        #         cache[i] = 0
        #         return cache[i]

        #     cache[i] = dfs(i + 1)
        #     if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
        #         cache[i] += dfs(i + 2)

        #     return cache[i]

        # return dfs(0)

        # ---------------------------
        # base case is 1, so i can build from that ?
        # i can move from 0 to n basically 
        # same state conversion

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1): # stops at n
            # take 1 element
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
            