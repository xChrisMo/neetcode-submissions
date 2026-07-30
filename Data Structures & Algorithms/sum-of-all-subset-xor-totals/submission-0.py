class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        out = []
        subset = []

        # for each index
        # do a XOR of that number and the other numbers 
        # 

        def dfs(i, current_xor):
            if i == len(nums):
                return current_xor

            include = dfs(i + 1, current_xor ^ nums[i])
            exclude = dfs(i + 1, current_xor)

            return include + exclude

        return dfs(0, 0)

        # return sum(out)
