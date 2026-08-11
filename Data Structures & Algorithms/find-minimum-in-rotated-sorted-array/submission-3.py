class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(m):
            return nums[m] < nums[-1]

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m

            else:
                l = m + 1

        return nums[l]