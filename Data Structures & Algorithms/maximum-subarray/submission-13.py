class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s = float('-inf')
        running_sum = 0
        n = len(nums)

        for i in range(n):
            if running_sum < 0:
                running_sum = 0
            running_sum += nums[i]
            max_s = max(max_s, running_sum)

        return max_s