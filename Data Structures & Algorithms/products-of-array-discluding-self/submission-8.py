class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # out=[]
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             prod*=nums[j]
        #     out.append(prod)
        # return out

        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
