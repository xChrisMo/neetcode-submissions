class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}

        for char in nums:
            count_dict[char] = count_dict.get(char, 0) + 1

        return max(count_dict, key=count_dict.get)