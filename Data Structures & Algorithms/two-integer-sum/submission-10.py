class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1st thought. for each index, loop to see if we get another index that adds to target
        # 2nd. Use a dict to find reminder meeded to sum to the target

        # ONLY ONE VALID ANSWER ? sorted ?
        # answer with i, before j

        # use a dict to store the diff, store the diff -> index in dict
        # for each number, check if the smaller number already inside the dict
        # o(n) time and space

        dict_nums = dict()

        for i, num in enumerate(nums):
            diff = target - num

            if diff in dict_nums:
                return [dict_nums[diff], i]

            dict_nums[num] = i


            