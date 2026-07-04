class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        # [1,2,3,4,5,6,7,8]
        # [8,7,6,5,4,3,2,1]

        #[5,6,7,8,4,3,2,1]
        #[5,6,7,8,1,2,3,4]

        # nums[:] = nums[-k:n] + nums[:-k]

        def reverse(nums: List[int], l: int, r: int) -> List[int]:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

            return nums

        reverse(nums, 0, n - 1) # reverse 0-7
        reverse(nums, 0, k - 1) # if k == 4, reverse/flip 0 - 3 
        reverse(nums, k, n - 1) # if k == 4, reverse/flip 4-7