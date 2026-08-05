class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_dict = {0:1}
        curSum = 0
        res = 0

        for num in nums:
            curSum += num
            diff = curSum - k
            res += count_dict.get(diff, 0)

            count_dict[curSum] = count_dict.get(curSum, 0) + 1

        return res