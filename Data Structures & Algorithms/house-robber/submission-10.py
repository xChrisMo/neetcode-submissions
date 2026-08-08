class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} #i->val
        def dfs(i):
            if i in memo:
                return memo[i]
                
            if i >= len(nums):
                memo[i] = 0
                return memo[i]

            take = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)

            memo[i] = max(take, skip)
            return memo[i]

        return dfs(0)