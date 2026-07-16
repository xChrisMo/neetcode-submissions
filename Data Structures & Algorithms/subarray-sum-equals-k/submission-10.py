class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0:1}
        running_sum = 0
        count_k = 0

        for num in nums:
            running_sum += num
            diff = running_sum - k

            count_k += sum_dict.get(diff, 0)

            sum_dict[running_sum] = sum_dict.get(running_sum, 0) + 1


        return count_k