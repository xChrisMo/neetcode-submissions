class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)


        dict_nums = {}

        for num in nums:
            if num in dict_nums:
                return num

            dict_nums[num] = 1 

        