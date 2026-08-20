class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(k):
            return nums[k]>=target
        
        l=0
        r=len(nums)-1
        while l<r:
            m=l +((r-l)//2)
            if condition(m):
                r=m
            else:
                l=m+1
        return l if nums[l]==target else -1