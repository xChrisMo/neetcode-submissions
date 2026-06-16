class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                n = max(n,cnt)
                cnt = 0
            else:
                cnt +=1
        return max(n,cnt)
