class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(i + num, max_reach)

            if max_reach >= len(nums) - 1:
                return True

        return False