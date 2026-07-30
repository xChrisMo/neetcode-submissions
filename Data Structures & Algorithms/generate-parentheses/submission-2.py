class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if open_n < n,
        # push '('

        # if closed_n < open_n:
        # push ')'

        out = []
        subset = []

        def dfs(i, opened_n, closed_n):
            # if terminal, add an open
            if n == opened_n == closed_n:
                out.append(''.join(subset[:]))
                return 

            if opened_n < n:
                subset.append('(')
                dfs(i + 1, opened_n + 1, closed_n)
                subset.pop()
            # if open < closed, do a closed

            if closed_n < opened_n:
                subset.append(')')
                dfs(i + 1, opened_n, closed_n + 1)
                subset.pop()

        dfs(0, 0, 0)
        return out