class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set... if seen -= , keep moving, compare that with longest
        # use a seen for o(1) checks

        longest = 0
        numset = set(nums)

        for num in nums:
            if (num - 1) not in numset:
                length = 1
                while (num + length) in numset:
                    length += 1
                longest = max(longest, length)

        return longest