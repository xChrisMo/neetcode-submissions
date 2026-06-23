class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        if n in memo:
            return memo[n]

        #we start from 3
        i = 3

        while i <= n:
            memo[i] = memo[i - 1] + memo[i - 2]
            i += 1
        
        # when i == n, we break out, so we simply return 
        return memo[n]
