class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def cond(k):
            return nums[k]>=target
        
        l=0
        r=len(nums)
        while l<r:
            m=l+ ((r-l)//2)
            if cond(m):
                r=m
            else:
                l=m+1
        print(l)
        return l

        

