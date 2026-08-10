class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False
        cache = {}
        def dfs(i, j):
            # if i at the end, return False
            # if j at the end, return False
            # if i at end and j at end, and s3 at i and j, return True
            # if only s1[i] matches, we go dfs(i + 1, j)
            # if s2[j], we go dfs(i, j + 1)
            # if neither return False
            if (i, j) in cache:
                return cache[(i, j)]
            ans = False

            if i == m and j == n:
                return True

            if i < m and s1[i] == s3[i + j]:
                ans = ans or dfs(i + 1, j)

            if j < n and s2[j] == s3[i + j]:
                ans = ans or dfs(i, j + 1)

            cache[(i, j)] = ans
            return cache[(i, j)]

        return dfs(0, 0)