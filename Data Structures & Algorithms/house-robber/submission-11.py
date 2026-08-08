class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = {} #i->val
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]

        #     if i >= len(nums):
        #         memo[i] = 0
        #         return memo[i]

        #     take = nums[i] + dfs(i + 2)
        #     skip = dfs(i + 1)

        #     memo[i] = max(take, skip)
        #     return memo[i]

        # return dfs(0)
        n = len(nums)
        dp = [0] * (n + 1)
        
        # dp[0] is already 0
        # dp[1] is the first element in nums

        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            #dp[i] = #use previous only, use current and 2 back
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

        return dp[n]