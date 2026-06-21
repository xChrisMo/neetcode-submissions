class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        out = []

        def dfs(i, curr):
            if i == len(s):
                out.append(' '.join(curr))

            for j in range(i, len(s)):
                if s[i:j+1] in word_set:
                    curr.append(s[i:j+1])
                    dfs(j+1, curr)
                    curr.pop()

        dfs(0, [])
        return out