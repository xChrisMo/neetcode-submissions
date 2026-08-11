class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i >= n:
                cache[i] = 0
                return cache[i]

            take = dfs(i + 2) + nums[i]
            skip = dfs(i + 1)

            cache[i] = max(take, skip)
            return cache[i]
            
        return dfs(0)