class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(s: List[str]) -> bool:
            l = 0
            r = len(s) - 1
            while l < r: 
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            return True


        out = []

        def dfs(i, curSet):
            if i >= len(s):
                out.append(curSet[:])
                return 

            # include i
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    curSet.append(s[i:j+1])
                    dfs(j + 1, curSet)
                    curSet.pop()
            
        dfs(0, [])

        return out
            