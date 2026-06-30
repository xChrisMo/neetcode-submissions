class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [5, 1, 5, 3]
        # total = 14

        min_size = float('inf')
        l = total = 0
        n = len(nums)

        for r in range(n):
            total += nums[r]

            while total >= target:
                min_size = min(min_size, r - l + 1)
                total -= nums[l]
                l += 1
        
        return min_size if min_size != float('inf') else 0