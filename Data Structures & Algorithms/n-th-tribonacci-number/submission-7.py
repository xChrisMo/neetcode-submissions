class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}

        if n in memo:
            return memo[n]

        i = 3
        while i <= n:
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
            i += 1

        return memo[n]