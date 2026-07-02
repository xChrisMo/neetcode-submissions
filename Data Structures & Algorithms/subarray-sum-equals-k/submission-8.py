class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #i = 3
        #running_sum = 4
        #diff = 2
        
        #{0:1
        # 2:1
        # 1:1
        # 4:
        #}

        # count = 3

        subarray_dict = {0:1}
        running_sum = 0
        count = 0

        for r in range(len(nums)):
            running_sum += nums[r]
            diff = running_sum - k

            count += subarray_dict.get(diff, 0)

            subarray_dict[running_sum] = subarray_dict.get(running_sum, 0) + 1

        return count