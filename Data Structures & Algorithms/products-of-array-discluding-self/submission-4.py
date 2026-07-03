class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]

        # 48

        out = [0] * len(nums)

        for i in range(len(nums)): #every index
            prod = 1 #base product == 1
            for j in range(len(nums)): #for every index
                if i == j: #if our inner loop sees our i,
                    continue #we continue
                else:
                    prod *= nums[j] #else, that 1 i, we use all other indexes 
            out[i] = prod #replace nums[i] with the product, it resets to 0 after the inner loop

        return out
