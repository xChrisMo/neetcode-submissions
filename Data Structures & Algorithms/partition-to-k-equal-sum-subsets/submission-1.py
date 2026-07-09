class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0: return False

        target = sum(nums) // k
        sides = [0] * k
        nums.sort(reverse=True)

        def backtrack(i):
            # base condition really
            if i == len(nums):
                return True

            for j in range(k):
                if nums[i] + sides[j] <= target:
                    sides[j] += nums[i]
                    if backtrack(i + 1) == True:
                        return True

                    sides[j] -= nums[i]
            
                if sides[j] == 0: 
                    break

            return False

        return backtrack(0)