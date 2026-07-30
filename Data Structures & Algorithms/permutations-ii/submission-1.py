class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        subset = []
        used = [False] * len(nums)

        def dfs():
            if len(subset) == len(nums):
                out.append(subset[:])
                return 

            for j in range(len(nums)):
                if used[j]:
                    continue 
                if j > 0 and nums[j] == nums[j - 1] and used[j - 1] == True:
                    continue

                used[j] = True
                subset.append(nums[j])
                dfs()

                used[j] = False
                subset.pop()


        dfs()
        return out