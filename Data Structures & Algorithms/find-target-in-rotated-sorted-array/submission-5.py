class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(i):
            # if it is on the left
            mid_sorted = nums[i] >= nums[0]
            target_sorted = target >= nums[0]

            if mid_sorted == target_sorted:
                # middle greater than target
                return nums[i] >= target

            # if only the the mid_is sorted left and not the target in that range
            elif mid_sorted:
                return False

            else:
                return True

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m

            else:
                l = m + 1

        if nums[l] == target:
            return l

        return -1