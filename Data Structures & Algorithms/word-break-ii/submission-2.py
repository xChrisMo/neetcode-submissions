class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # bruteforce. check if every word fits inside s
        out = []
        subset = []
        wordset = set(wordDict)

        def dfs(i):
            if i == len(s):
                out.append(' '.join(subset[:]))
                return 

            for j in range(i, len(s)):
                # basically if word in worddict
                if s[i:j+1] in wordset:
                    # add it to subset
                    subset.append(s[i:j+1])
                    # recursively move pointer to find other wirds
                    dfs(j + 1)

                    subset.pop()

        dfs(0)
        return out