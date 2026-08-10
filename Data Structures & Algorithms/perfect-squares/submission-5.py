class Solution:
    def numSquares(self, n: int) -> int:
        # bruteforce it all
        # for i in range(n // 2)
        # if i ** 1/2 % 2 == 0
        # cache it
        # cache = {}
        # def dfs(i):
        #     if i in cache: return cache[i]

        #     if i == 0:
        #         cache[i] = 0
        #         return cache[i]

        #     res = float('inf')
        #     for j in range(1, n + 1):
        #         square = j * j

        #         # out of bound
        #         if square > i:
        #             break

        #         res = min(res, 1 + dfs(i - square))
        #         cache[i] = res
            
        #     return cache[i]
        
        # return dfs(n)
        
        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            # j should be between 0 and i 
            for j in range(1, i + 1):
                square = j * j
                if square <= n:
                    dp[i] = min(dp[i], 1 + dp[i - square])

                else:
                    break
        
        return dp[n]