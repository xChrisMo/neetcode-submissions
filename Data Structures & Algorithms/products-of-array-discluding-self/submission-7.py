class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use a double for looop, and then a variable !

        # out = []
        # for i in range(len(nums)):
        #     stand = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         stand *= nums[j]
        #     out.append(stand)

        # return out

        # a more efficient way is a forward and backward sacn
        # forward :[1, 1, 2, 8]
        # backward:[48,24,6,1]
        out = []

        forward_int = 1
        for i in range(len(nums)):
            out.append(forward_int)
            forward_int *= nums[i]


        back_int = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= back_int
            back_int *= nums[i]

        return out
