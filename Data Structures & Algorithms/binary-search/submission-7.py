class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(m):
            if nums[m] >= target:
                return True

        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m

            else:
                l = m + 1

        if l < len(nums) and nums[l] == target:
            return l

        return -1