class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # for index, num in nums
        # if sum >= last_index, return True
        target = len(nums) - 1
        max_reach = 0

        for i, num in enumerate(nums):
            if i > max_reach:
                return False

            if max_reach >= target:
                return True
            # / move forward
            max_reach = max(max_reach, num + i)
