class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        i need to move, and check if each index i in t, if not move
        if in t, move both i and j
        if not, move j
        if i == len(s), return True
        if j == len(t), return False
        '''
        i = 0
        j = 0

        def dfs(i, j):
            if i == len(s):
                return True

            elif j == len(t):
                return False

            if s[i] == t[j]:
                return dfs(i + 1, j + 1)

            if s[i] != t[j]:
                return dfs(i, j + 1)

        return dfs(0, 0)
        