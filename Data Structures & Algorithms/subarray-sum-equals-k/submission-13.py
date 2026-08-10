class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        diff_map = {0:1}
        curSum = 0
        res = 0

        for num in nums:
            curSum += num
            diff = curSum - k

            res += diff_map.get(diff, 0)

            diff_map[curSum] = 1 + diff_map.get(curSum, 0)

        return res