class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0

        globalMin = nums[0]
        globalMax = nums[0]
        
        total = 0
        
        for num in nums:
            total += num
            curMax = max(num, curMax + num)
            curMin = min(num, curMin + num)

            globalMin = min(globalMin, curMin)
            globalMax = max(globalMax, curMax)


        if globalMax < 0:
            return globalMax

        else:
            return max(globalMax, total - globalMin)