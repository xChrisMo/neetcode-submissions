class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1

                else:
                    return False

            return True

        curset = []
        out = []

        def dfs(i):
            if i == len(s):
                out.append(curset[:])
                return 

            # do backtracking after it a valid pandrime
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    curset.append(s[i:j + 1])
                    dfs(j + 1)
                    curset.pop()

        dfs(0)
        return out