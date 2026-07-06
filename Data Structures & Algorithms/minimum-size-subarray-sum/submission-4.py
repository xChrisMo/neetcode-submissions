class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        running_sum = 0
        l = 0
        min_sub = float('inf')

        # 2, 3, 8, 9, 14, 17
        for r in range(len(nums)):
            running_sum += nums[r]

            while running_sum >= target:
                min_sub = min(min_sub, r - l + 1)
                running_sum -= nums[l]
                l += 1



        return min_sub if min_sub != float('inf') else 0