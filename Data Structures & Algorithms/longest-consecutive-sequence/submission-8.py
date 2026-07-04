class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # lenght = float('-inf')
        set_nums = set(nums)
        l = 0

        for num in set_nums:
            if (num - 1) not in set_nums:
                # we have found a start here
                length = 0

                while (num + length) in set_nums:
                    length += 1

            
                l = max(l, length)

        return l