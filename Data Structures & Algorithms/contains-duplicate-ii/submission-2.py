class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # we can use a dict
        # we can use a window
        # we can use a set

        l = 0
        n = len(nums)
        seen = set()

        for r in range(n):
            if nums[r] in seen:
                return True

            seen.add(nums[r])

            while r - l + 1 > k:
                seen.remove(nums[l])
                l += 1

        return False