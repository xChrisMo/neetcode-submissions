class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique = set(nums)
        out = []

        for i in range(1, len(nums) + 1):
            if i not in unique:
                out.append(i)


        return out