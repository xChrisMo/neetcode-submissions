class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort, find the one in the middle (very shaky!)
        # use a dictionary
        # use the condition they gave....

        nums.sort()
        n = len(nums)

        return nums[n//2]