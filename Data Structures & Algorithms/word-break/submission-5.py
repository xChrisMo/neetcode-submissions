class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # s
        # wordDict

        #return true if s can be broken down into wordDicts values

        #reuse dict as many times as long as s remains....

        wordset = set(wordDict)
        print(type(wordset))
        print(wordset)

        # dp ? memoize ?
        # basically if i == len(s): return True
        # else if we cant find that index in ANY words of wordDict, return False
        # we need a terminal condition for passing everyword dict...
        
        #  use worddict as a set
        # dfs(i):
        #base condition if i == len(s): return True
        # for j in range(i, len(s)) 
        # if s[i:i+j] == w and i:i+j< len(s):
        #return trure
        #return false
        memo = {len(s):True} #adding the base condition

        def dfs(i):
            #base case, when we get to the end
            if i in memo:
                return memo[i]

            if i == len(s):
                return memo[i]

            for j in range(i, len(s)):
                if s[i:j+1] in wordset:
                    if dfs(j + 1):
                        memo[i] = True
                        return memo[i]

            memo[i] = False
            return memo[i]

        return dfs(0)