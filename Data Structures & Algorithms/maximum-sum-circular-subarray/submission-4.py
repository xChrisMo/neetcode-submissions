class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sub = float('-inf')
        n = len(nums)

        # bruteforce for normal array
        # for i in range(n):
        #     cur_sum = 0
        #     for j in range(i, n):
        #         cur_sum += nums[j]
        #         max_sub = max(max_sub, cur_sum)

        # return max_sub

        # kadane using a running sum
        # running_sum = 0
        # for num in nums:
        #     running_sum += num
        #     max_sub = max(running_sum, max_sub)

        #     if running_sum < 0:
        #         running_sum = 0

        # return max_sub

        # for circular, we can make the kadane a function, and do max between this range and that range ? give clues please 

        #[-2,4,-5,4,-5,9,4]

        # for i in range(n):
        #     cur_sum = 0

        #     for j in range(i, i + n):
        #         cur_sum += nums[j % n]
        #         max_sub = max(max_sub, cur_sum)
            
        # return max_sub

        curMin = 0
        curMax = 0

        globalMin = nums[0]
        globalMax = nums[0]
        total = 0

        for num in nums:
            total += num
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)

            globalMin = min(curMin, globalMin)
            globalMax = max(curMax, globalMax)

        # all negatives, 
        if globalMax < 0:
            return globalMax

        else:
            return max(globalMax, total - globalMin)