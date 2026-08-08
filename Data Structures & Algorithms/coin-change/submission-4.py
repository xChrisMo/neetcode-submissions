class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = {} # (i, r_s) -> 

        # n = len(coins)
        # def dfs(i, r_s):
        #     if (i, r_s) in memo:
        #         return memo[(i, r_s)]

        #     # breaks, out of bounds 
        #     if r_s == amount:
        #         return 0

        #     if i == n or r_s > amount:
        #         return float('inf')

        #     # skip
        #     skip = dfs(i + 1, r_s)

        #     # take
        #     take = 1 + dfs(i, r_s + coins[i])

        #     memo[(i, r_s)] = min(skip, take)
        #     return memo[(i, r_s)]

        # ans = dfs(0, 0)
        # return ans if ans != float('inf') else -1 

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return -1 if dp[amount] == float('inf') else dp[amount]

            # write take
            # take = NO IDEA
            # write skip
            # skip = NO IDEA
            # return minimum of those

        # if dp[n] == inf, return -1, else return dp[n]