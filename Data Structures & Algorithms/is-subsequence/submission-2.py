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

        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
                
            if i == len(s):
                cache[(i, j)] = True
                return cache[(i, j)]

            elif j == len(t):
                cache[(i, j)] = False
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            if s[i] != t[j]:
                cache[(i, j)] = dfs(i, j + 1)
                return cache[(i, j)]

        return dfs(0, 0)


        