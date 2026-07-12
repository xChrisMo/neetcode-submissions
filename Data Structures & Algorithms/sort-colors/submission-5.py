class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort
        # make buckets of 0, 1, 2

        # do a merge sort, or do a bucket sort. 
        # since the values for num is either 0, 1, 2

        buckets = [0, 0, 0]

        # so i want to look at the num, add 1 to that index.
        # then from there, empty each bucket into array!

        for num in nums:
            buckets[num] += 1

        j = 0
        for i, count in enumerate(buckets):
            for _ in range(count):
                nums[j] = i
                j += 1


        # [1,2,1]
        
        # [0:1, 1:2, 2:1]
        
        # [1, 0, 1, 2]