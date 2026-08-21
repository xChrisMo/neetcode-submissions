class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        out = []
        curset = []

        def dfs(i, running_sum):
            if i == len(nums) or running_sum > target:
                return 

            if running_sum == target:
                out.append(curset[:])
                return 

            curset.append(nums[i])
            dfs(i, running_sum + nums[i])

            curset.pop()
            dfs(i + 1, running_sum)

        dfs(0, 0)
        return out