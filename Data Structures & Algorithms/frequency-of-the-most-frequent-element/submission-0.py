class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = total = freq = 0

        # basically if right * len(window) >= total + k: total -= nums[l], l += 1
        # freq = max(freq, r - l + 1)
        n = len(nums)

        for r in range(l, n):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
                
            freq = max(freq, r - l + 1)

        return freq