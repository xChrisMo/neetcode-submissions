class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # our answer can only be within 1 to n + 1
        # basically in range(1, n + 1)

        # [-2, -1, 0]
        # [1, 2, 3]

        # so between 1 and 4 
        # so if we see < 0, we set it to be 0

        # [-1, -2, 4]

        # if within range, 1, n, mark wheer we see each index
        # for each num, if abs(num) in range(1, n), nums[i] *= -1

        # for i in range(n), if nums[i + 1] > 0: return i + 1, else continue, return len(nums) + 1

        # 1. mark all negatives as -(len(nums)) + 2..
        # 2. check all index in array, if num[arr] > 0 and num[arr] < len(num) + 1, markits index by -1 if not already -1
        # 3. for loop from 1 to n + 1, if i + 1 > 0, return i + 1, else, continue, return len(nums) + 1

        n = len(nums)
        dummy = n + 2

        # step 1, if negative, or less than one, set to high dummy
        for i, num in enumerate(nums):
            if num < 1:
                nums[i] = dummy

        # step 2, if not dummy, and within 1 and n, mark its index as -1
        for i, num in enumerate(nums):
            val = abs(num)
            if 1 <= val <= n:
                if nums[val - 1] > 0: # if marked, just skip
                    nums[val - 1] *= -1
                else:
                    continue

        # step 3, checking from 0 to n - 1, we check if it is negative 
        for i in range(1, n+1):
            if nums[i - 1] > 0:
                return i

        # all integers in, return right of array nums
        return n + 1

            
