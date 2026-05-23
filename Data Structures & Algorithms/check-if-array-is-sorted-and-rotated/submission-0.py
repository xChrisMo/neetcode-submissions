class Solution:
    def check(self, nums: List[int]) -> bool:
        pivot = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                pivot += 1

        if nums[n - 1] > nums[0]:
            pivot += 1

        return pivot < 2