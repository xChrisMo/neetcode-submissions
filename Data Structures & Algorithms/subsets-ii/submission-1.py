class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        def dfs(i, curset):
            if i == len(nums):
                out.append(curset[:])
                return 

            curset.append(nums[i])
            dfs(i + 1, curset)
            curset.pop()

            j = i + 1
            while j > 0 and j < len(nums) and nums[i] == nums[j]:
                j += 1

            dfs(j, curset)

        dfs(0, [])
        return out