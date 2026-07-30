class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # so between 1, n
        # k possible numbers
        # i am thinking of checking a count of unique words. but then again, it would alwaus ne imqiue 

        out = []
        subset = []

        def dfs(i):
            if len(subset) == k:
                out.append(subset[:])
                return 

            # out of bounds
            if i > n:
                return 

            subset.append(i)
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(1)
        return out