class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        [3 4 5 6]
        target =7
        {3:0, }


        '''
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        resMap={}
        for index,val in enumerate(nums):
            diff=target-val
            if diff in resMap:
                return [resMap[diff],index]
            resMap[val]=index
    


            