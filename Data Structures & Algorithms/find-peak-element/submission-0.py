class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # max_val = float('-inf')
        # maxi = 0

        # for i in range(len(nums)):
        #     if nums[i] > max_val:
        #         max_val = nums[i]
        #         maxi = i

        # return maxi

        # how can i do a BS on a non monotonic array ?
        # if has to be a bruteforce/double check. 
        def condition(m):
            return nums[m] < nums[m + 1]

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if condition(m):
                l = m + 1

            else:
                r = m

        return l