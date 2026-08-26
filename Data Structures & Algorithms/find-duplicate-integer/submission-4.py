class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        slow 2
        fast 2
        slow1 4
        '''
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow1=0
        while slow1!=slow:
            slow=nums[slow]
            slow1=nums[slow1]
        return slow


        

        