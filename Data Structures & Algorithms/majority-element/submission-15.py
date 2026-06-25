class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort, find the one in the middle (very shaky!)
        # use a dictionary
        # use the condition they gave....

        # A. sort, find the one in the middle (very shaky!)
        # nums.sort()
        # n = len(nums)

        # return nums[n//2]

        # B. use a dictionary
        dict_nums = {}

        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1

        return max(dict_nums, key=dict_nums.get)