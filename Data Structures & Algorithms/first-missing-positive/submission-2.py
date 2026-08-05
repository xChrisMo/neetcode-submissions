class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # basically go through all
        # if nefative, set to 0
        # [1, 2, 4] still 124
        # one pass, for num in nums, 
        # if num in range, 
        # max_v = len(nums) + 2
        # abs(num) - 1 *= -max_v

        max_v = float('-inf')   
        n = len(nums)

        # negative marking
        for i, num in enumerate(nums):
            max_v = max(max_v, num)
            if nums[i] <= 0:
                nums[i] = n + 1

        max_v += 2
        for i, num in enumerate(nums):
            val = abs(num)
            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1