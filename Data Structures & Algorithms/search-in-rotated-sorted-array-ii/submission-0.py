class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # similar really
        # if target <= left
        # if mid <= left

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target == nums[m]:
                return True

            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1

            # left sorted portion
            elif nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1

                else:
                    r = m - 1

            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1

                else:
                    l = m + 1

        return False