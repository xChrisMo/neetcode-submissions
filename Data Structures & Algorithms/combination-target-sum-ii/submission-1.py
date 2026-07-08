class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []

        def subsets(i, total, curSet):
            # if total == target, good. WE CHECK IF BEFORE I > LEN(CANd) cos we know we should find
            if total == target:
                out.append(curSet[:])
                return 

            # out of bounds, either i or total
            if i >= len(candidates) or total > target:
                return 

            # inlcude i
            curSet.append(candidates[i])
            subsets(i + 1, total + candidates[i], curSet)
            curSet.pop()

            # exclude i
            j = i + 1

            # if we havent gotten to len candiates, and i, prev == next, go to next
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1

            subsets(j, total, curSet)


        subsets(0, 0, [])
        return list(out)