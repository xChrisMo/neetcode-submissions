class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {}

        def dfs(i, cur):
            if (i, cur) in cache:
                return cache[(i, cur)]

            if i == n:
                if cur == target:
                    cache[(i, cur)] = 1
                    return cache[(i, cur)]

                cache[(i, cur)] = 0
                return cache[(i, cur)]

            add = dfs(i + 1, cur + nums[i])
            remove = dfs(i + 1, cur - nums[i])

            cache[(i, cur)] = add + remove
            return cache[(i, cur)]
            
        return dfs(0, 0)