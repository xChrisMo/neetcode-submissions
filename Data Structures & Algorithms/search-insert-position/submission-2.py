class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # we want to look for the first number nearest to it
        # condition should be, if greater than, r = m, we penalise the right more
        # we return the left most

        def condition(i):
            if nums[i] >= target:
                return True

        n = len(nums)
        l = 0
        r = n

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m

            else:
                l = m + 1

        return l

