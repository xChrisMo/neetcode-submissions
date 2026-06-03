class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(num_set)

        for i in range(n + 1):
            if i not in nums:
                return i