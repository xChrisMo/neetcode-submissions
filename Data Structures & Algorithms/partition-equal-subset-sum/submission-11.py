class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        # n = len(nums)
        # cache = {} # (i, running_sum)
        # # cache[(i, running_sum)]

        # def dfs(i, running_sum):
        #     if (i, running_sum) in cache:
        #         return cache[(i, running_sum)]

        #     if running_sum > target or i == n:
        #         cache[(i, running_sum)] = False
        #         return cache[(i, running_sum)]

        #     if running_sum == target:
        #         cache[(i, running_sum)] = True
        #         return cache[(i, running_sum)]

        #     # skip
        #     skip = dfs(i + 1, running_sum)

        #     # take
        #     take = dfs(i + 1, running_sum + nums[i])

        #     cache[(i, running_sum)] = skip or take
        #     return cache[(i, running_sum)]

        # return dfs(0, 0)

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

        # [2, 8, 10]
        #