class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        number_ones = 0
        l = 0
        max_ones = 0
        # n = len

        for r in range(len(nums)):
            if nums[r] == 1:
                number_ones += 1

            while (r - l + 1) - number_ones > 1:
                if nums[l] == 1:
                    number_ones -= 1

                l += 1

            max_ones = max(max_ones, (r - l + 1))

        return max_ones