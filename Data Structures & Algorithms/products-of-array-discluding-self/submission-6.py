class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use a double for looop, and then a variable !

        out = []
        for i in range(len(nums)):
            stand = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                stand *= nums[j]
            out.append(stand)

        return out