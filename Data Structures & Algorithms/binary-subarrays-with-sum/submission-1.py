class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # [1,0,1,0,1]
        # 3

        #{0:1
        # 1:2
        # 2:1
        # 

        # 1 + 1 + 2
        # forward scan, add next element, have a 'total' variable
        # while total > goal: remove left from total, shift l
        # if total == goal: count += 1

        total = 0
        running_sum = 0
        seen = {0:1} # at start, sum = 0

        for r in range(len(nums)):
            running_sum += nums[r]

            diff = running_sum - goal

            total += seen.get(diff, 0)

            seen[running_sum] = seen.get(running_sum, 0) + 1

        return total