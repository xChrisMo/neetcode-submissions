class Solution:
    def countSubstrings(self, s: str) -> int:
        # def dfs(i):
        #     # single letter would always be a palindrome
        #     if i == len(s):
        #         return 1
        n = len(s)
        res = 0

        for i in range(n):
            l = i
            r = i

            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res