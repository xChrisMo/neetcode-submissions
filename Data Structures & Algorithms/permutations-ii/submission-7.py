class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        used = [False] * n
        out = []
        subset = []

        def dfs(i):
            if i == n:
                out.append(subset[:])
                return 

            for j in range(n):
                if used[j] == True:
                    continue

                if j > 0 and nums[j] == nums[j - 1] and used[j - 1] == True:
                    continue

                used[j] = True
                subset.append(nums[j])

                dfs(i + 1)
                
                used[j] = False
                subset.pop()

        dfs(0)
        return out