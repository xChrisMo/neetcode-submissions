class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # starting from n - 2, we want to check if the element to the right is greater, 
        # if not, we know we have reached some maximum, we flip round!
        # if we do find a place where n - 2 < n - 1, that n - 2 is our index
        # then we start from our right again, to swap index from first lesser than from right!
        # after the swap, from pivot + 1 to end, we reverse
        n = len(nums)
        i = n - 2

        pivot = None

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1 # move inwards

        pivot = nums[i]

        # if no pivot is found
        if i < 0:
            nums.reverse()
            return

        # look for next lesser element from right

        for j in range(n - 1, i-1, -1): #from last element till i
            if nums[j] > nums[i]:
                break

        nums[j], nums[i] = nums[i], nums[j]

        l = i + 1
        r = n - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        