class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        subset = []
        nums.sort()

        def dfs(i):
            # terminal 
            # add to curset
            # 
            if i == len(nums):
                out.append(subset[:])
                return 

            # add to subset
            subset.append(nums[i])
            # backtrack
            dfs(i + 1)
            # pop
            subset.pop()
            # check for duplicates
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)
        return out