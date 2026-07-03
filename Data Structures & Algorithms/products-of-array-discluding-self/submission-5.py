class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]

        # 48

        # out = [0] * len(nums)

        # for i in range(len(nums)): #every index
        #     prod = 1 #base product == 1
        #     for j in range(len(nums)): #for every index
        #         if i == j: #if our inner loop sees our i,
        #             continue #we continue
        #         else:
        #             prod *= nums[j] #else, that 1 i, we use all other indexes 
        #     out[i] = prod #replace nums[i] with the product, it resets to 0 after the inner loop

        # return out

        # [1, 1, 2, 8]

        # [48, 24, 6, 1]
        
        prefix_product = 1
        prefix_arr = []

        for i in range(len(nums)):
            prefix_arr.append(prefix_product)
            prefix_product *= nums[i]

        suffix_product = 1
        suffix_arr = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            suffix_arr[i] = suffix_product
            suffix_product *= nums[i]

        out = [1] * len(nums)

        for i in range(len(nums)):
            out[i] = suffix_arr[i] * prefix_arr[i]

        return out