class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        cache = {}
        
        # start, stop
        def dfs(i, n):
            if (i, n) in cache:
                return cache[(i, n)]

            if i > n:
                cache[(i, n)] = 0
                return cache[(i, n)]

            take = nums[i] + dfs(i + 2, n)
            skip = dfs(i + 1, n)

            cache[(i, n)] = max(take, skip)
            return cache[(i, n)]

        return max(dfs(0, n-2), dfs(1, n-1))