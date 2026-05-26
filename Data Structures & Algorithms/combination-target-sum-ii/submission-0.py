class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #sort it all out
        candidates.sort()
        out = []
        subset = []

        def backtrack(i, total):
            # base condition
            if total == target:
                out.append(subset[:])
                return 

            # overflow (either target or index)
            if total > target or i >= len(candidates):
                #continue? #cant use cos continue only works for for-while loops 
                return 

            #include current index
            subset.append(candidates[i])
            #backtrack from current index
            backtrack(i + 1, total + candidates[i])
            #real backtracking
            subset.pop()

            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            
            backtrack(j, total)
            

        #calling backtrack from first index and 0 total?
        backtrack(0, 0)

        return out