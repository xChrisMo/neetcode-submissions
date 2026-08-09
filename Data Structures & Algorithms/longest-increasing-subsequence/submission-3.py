class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # i am thinking of going from 0 index to n - 1 index
        # for each index, i want to only see if next index is greater than it?
        n = len(nums)
        cache = {} # (i,)

        def dfs(i):
            # base case, return 0
            if i in cache:
                return cache[i]

            if i == n:
                cache[i] = 0
                return cache[i]

            best = 1 

            for j in range(i + 1, n):
                # skip-ish
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            cache[i] = best
            return cache[i]

        return max([dfs(i) for i in range(n)])