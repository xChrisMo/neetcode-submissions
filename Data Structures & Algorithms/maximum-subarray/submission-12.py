class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = float('-inf')
        running_sum = 0
        n = len(nums)

        for num in nums:
            running_sum += num
            max_sub = max(max_sub, running_sum)

            if running_sum < 0:
                running_sum = 0

        return max_sub