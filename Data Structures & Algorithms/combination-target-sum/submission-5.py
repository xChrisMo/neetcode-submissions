class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []

        def dfs(i, total, subSet):
            if total == target:
                out.append(subSet[:])
                return 

            if total > target or i == len(nums):
                return 

            # include i, we need to make it keep running somehow, key is in the i in dfs, we keep using the same i
            subSet.append(nums[i])
            dfs(i, total + nums[i], subSet)

            # not include i
            subSet.pop()
            dfs(i + 1, total, subSet)

        dfs(0, 0, [])
        return out