class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        subset = []
        visited = set()

        def backtrack():
            if len(subset) == len(nums):
                out.append(subset[:])
                return 

            for i in range(len(nums)):
                if i in visited:
                    continue 

                if i > 0 and nums[i - 1] == nums[i] and (i - 1) in visited:
                    continue 

                visited.add(i)
                subset.append(nums[i])
                backtrack()

                subset.pop()
                visited.remove(i)
        backtrack()
        return out