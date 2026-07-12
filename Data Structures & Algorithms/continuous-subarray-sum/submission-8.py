class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #[23, 25, 29, 35, 42]
        # dict_nums = {0:-1} #if first is 0, we put -1. so i - - 1 would always be 
        # running_sum = 0

        # for i, num in enumerate(nums):
        #     #increase running_sum
        #     running_sum += num

        #     #get reminder
        #     val = running_sum % k

        #     #chekc if reminder is stored
        #     if val in dict_nums:
        #         if i - dict_nums[val]> 1:
        #             return True

        #     #store reminder with an index if not seen
        #     else:
        #         dict_nums[val] = i

        # return False

        for i in range(len(nums)):
            cur_sum = nums[i]
            for j in range(i + 1, len(nums)):
                cur_sum += nums[j]

                if cur_sum % k == 0:
                    return True

        return False