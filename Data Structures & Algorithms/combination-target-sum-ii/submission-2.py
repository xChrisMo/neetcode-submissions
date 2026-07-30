class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        out = []
        subset = []

        def dfs(i, running_sum):
            # if sum == target, append subset copy, return 
            # if i >= len(candidates) or sum > target: return 
            # include. dfs(i + 1, running_sum + candidates[i])
            # exclude. j = i + 1. while candidates[j] == candidates[i] and j < len(candidates), j += 1
            # dfs(j, running_sum)

            if running_sum == target:
                out.append(subset[:])
                return 

            if i >= len(candidates) or running_sum > target:
                return 

            # include 
            subset.append(candidates[i])
            dfs(i + 1, running_sum + candidates[i])

            # exclude
            j = i + 1
            
            subset.pop()
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            dfs(j, running_sum)

        dfs(0, 0)
        return out