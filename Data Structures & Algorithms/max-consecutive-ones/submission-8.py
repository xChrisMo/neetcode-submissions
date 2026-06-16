class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                maxOnes = max(maxOnes,count)
                count = 0
            else:
               
                count +=1
        return max(maxOnes, count)
        