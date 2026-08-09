class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {} #(i, cur)
        # cache[(i, cur)]

        def dfs(i, cur):
            if (i, cur) in cache:
                return cache[(i, cur)]
            # cur == target
            if cur == target:
                cache[(i, cur)] = 1
                return cache[(i, cur)]

            # out of bound 
            if i == n or cur > target:
                cache[(i, cur)] = 0
                return cache[(i, cur)]

            skip = dfs(i + 1, cur)
            take = dfs(0, cur + nums[i])

            cache[(i, cur)] = skip + take
            return cache[(i, cur)]

        return dfs(0, 0)