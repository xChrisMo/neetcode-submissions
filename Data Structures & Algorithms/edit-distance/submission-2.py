class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        cache = {}


        def dfs(i, j):
            # if i == m: return 0
            # if j == n: return 0
            # if they match, dfs(i + 1, j + 1)
            # if no match, replace
            # replcae is the same as match, delete is moving i, replcae is moving j
            # FIND ZE MINIMUM !
            if (i, j) in cache:
                return cache[(i, j)]

            if i == m:
                return n - j

            if j == n:
                return m - i

            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            insert = dfs(i + 1, j)
            delete = dfs(i, j + 1)
            replace = dfs(i + 1, j + 1)

            cache[(i, j)] = 1 + min(insert, delete, replace)
            return cache[(i, j)]
            
        return dfs(0, 0)