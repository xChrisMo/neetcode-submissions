class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # create a palindrome function
        # if palindrome, go more
        # put into dummy, if i == len(s)
        # add to the result list
        # 

        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        out = []
        res = []

        def dfs(i):
            # if we get to the last index, we know they're all palindromes
            if i == len(s):
                out.append(res[:])
                return 

            # res is where we store old additions
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    res.append(s[i:j+1])
                    dfs(j + 1)
                    res.pop()

        dfs(0)
        return out