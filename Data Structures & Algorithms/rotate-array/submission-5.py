class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        # [1,2,3,4, 5,6,7,8]

        print(k)
        #rotated bit + rests
        # rotated bit == nums[k:n]
        # rests == nums[:k]

        nums[:] = nums[-k:n] + nums[:-k]