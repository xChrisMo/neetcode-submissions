class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(res,count)
                count = 0
            else:
                count +=1
        return max(count, res)


        