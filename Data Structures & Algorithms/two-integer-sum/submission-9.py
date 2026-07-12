class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1st thought. for each index, loop to see if we get another index that adds to target
        # 2nd. Use a dict to find reminder meeded to sum to the target

        # ONLY ONE VALID ANSWER ?
        # answer with i, before j
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]