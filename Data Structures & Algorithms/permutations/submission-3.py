class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        out = []
        subset = []

        def dfs(i):
            if len(subset) == len(nums):
                out.append(subset[:])
                return 

            for j in range(len(nums)):
                if used[j] == True:
                    continue

                # else, mark it, 
                # use it
                used[j] = True
                subset.append(nums[j])

                dfs(i + 1)

                used[j] = False
                subset.pop()

        dfs(0)
        return out
