class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # make buckets, [][][]
        # use a loop, to match the value to an index at that value
        # keep increasing the count of each bucket
        # make another pass to fill it out into nums

        buckets = [0] * 3

        for i, num in enumerate(nums):
            buckets[num] += 1

        # buckets = [1, 2, 1]
        i = 0
        for color, count in enumerate(buckets):
            # add that color to that index in nums
            while count > 0:
                nums[i] = color
                i += 1
                count -= 1




        