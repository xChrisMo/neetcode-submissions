class Solution:
    def tribonacci(self, n: int) -> int:
        # memo = {0:0, 1:1, 2:1}

        # if n in memo:
        #     return memo[n]

        # i = 3
        # while i <= n:
        #     memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        #     i += 1

        # return memo[n]
        if n <= 2:
            return 1 if n != 0 else 0

        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]