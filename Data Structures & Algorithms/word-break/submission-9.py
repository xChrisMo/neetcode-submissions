class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        # cache = {}

        # def dfs(i):
        #     # terminal check 
        #     if i in cache:
        #         return cache[i]
                
        #     if i == n:
        #         return True

        #     # from any i index
        #     for j in range(i, n):
        #         # if we look from i to j and it is in worset
        #         if s[i:j + 1] in wordSet: # remember slicing is exclusive, so i added + 1
        #             # if from j to the end is also in the set
        #             if dfs(j + 1) == True:
        #                 # return True
        #                 cache[i] = True
        #                 return cache[i]

        #     cache[i] = False
        #     return cache[i]

        # return dfs(0)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # so every index is a Boolean
            for j in range(i):
                # for every index, we look forward in s
                if dp[j] == True and s[j:i] in wordSet:
                    # if looking back, it is in wordSet
                    dp[i] = True
                    # we set it to be true!

        return dp[n]