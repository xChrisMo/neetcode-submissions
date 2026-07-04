class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        out = []

        for char in s:
            if char.isalnum():
                out.append(char)

        out = ''.join(out)
        print(out)

        l = 0
        r = len(out) - 1

        while l < r:
            if out[l] != out[r]:
                return False
                
            else:
                l += 1
                r -= 1

        return True
