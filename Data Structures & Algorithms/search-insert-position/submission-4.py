class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums) 
        l = 0
        r = n

        # we are basically trying to minimizze the window!
        def condition(m):
            # if value > target, we know we can keep looking left
            # so if val < target, we move left + 1
            return nums[m] >= target

        while l < r:
            m = (l + r) // 2

            if condition(m):
                r = m

            else:
                l = m + 1 

        return l