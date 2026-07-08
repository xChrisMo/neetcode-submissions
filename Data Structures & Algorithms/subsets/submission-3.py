class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        
        def dfs(i, subset):
            if i == len(nums):
                out.append(subset[:])
                return 

            #include i
            subset.append(nums[i])
            dfs(i + 1, subset)

            #exclude i
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        return out