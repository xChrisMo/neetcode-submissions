class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        out_dict = {}

        for num in nums:
            out_dict[num] = out_dict.get(num, 0) + 1

        return max(out_dict, key=out_dict.get)