class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1

            return True

        subset = []
        out = []

        def backtrack(i):
            if i >= len(s):
                out.append(subset[:])
                return 

            #we pick up from that index till the end    
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    subset.append(s[i:j + 1])
                    backtrack(j + 1)

                    # backtrack here!
                    subset.pop()

        backtrack(0)
        return out