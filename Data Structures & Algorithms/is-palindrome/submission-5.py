class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = []
        for char in s:
            if char.isalnum():
                out.append(char.lower()) 


        l = 0
        r = len(out) - 1

        while l < r:
            if out[l] == out[r]:
                l += 1
                r -= 1

            else:
                return False

        return True