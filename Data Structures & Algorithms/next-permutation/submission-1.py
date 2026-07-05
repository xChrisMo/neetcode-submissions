class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1, 3, 2]

        #n = 3
        #i = n - 2, 
        #i = 1

        # from end to start, we keep going until we see an index where it is no longer increasing
        # 

        pivot = None
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 12354
        
        # found pivot at i 
        if i >= 0: #pivot found
            j = n - 1
            
            while nums[j] <= nums[i]:
                j -= 1 #until we find the next greater element

            nums[i], nums[j] = nums[j], nums[i]

        #we kinda know n would always be the end, else, the swao wiyld have happened earlier
        #nums[], nums[n] = nums[n], nums[pivot]

        # reverseing from afrtet pivot
        l = i + 1
        r = n - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # 