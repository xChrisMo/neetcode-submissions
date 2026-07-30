class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        out = []

        def dfs(i, running_sum):
            # if running_sum == target:
            # if running_sum > target: continue
            # add to the running_sum
            # dont add

            if running_sum == target:
                out.append(subset[:])
                return 

            if i >= len(nums) or running_sum > target:
                return 

            # grab this current index, add it to running_sum
            subset.append(nums[i])
            # recursively add that index, reuse
            dfs(i, running_sum + nums[i])

            # remove the value
            subset.pop()
            # recurisvley call dfs on same index
            dfs(i + 1, running_sum)

        dfs(0, 0)
        return out