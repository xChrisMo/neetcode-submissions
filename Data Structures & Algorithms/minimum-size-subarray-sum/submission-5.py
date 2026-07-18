class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float('inf')
        l = 0

        running_sum = 0

        for r in range(len(nums)):
            running_sum += nums[r]

            while running_sum >= target:
                min_size = min(min_size, r - l + 1)
                
                running_sum -= nums[l]
                l += 1


        return 0 if min_size == float('inf') else min_size