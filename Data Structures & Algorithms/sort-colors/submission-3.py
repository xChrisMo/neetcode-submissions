class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0,0,0] #making buckets for 0, 1, 2

        for num in nums:
            buckets[num] += 1

        i = 0
        for j, bucket in enumerate(buckets):
            while bucket > 0:
                nums[i] = j 
                bucket -= 1
                i += 1

        


        