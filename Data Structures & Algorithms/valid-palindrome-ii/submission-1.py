class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l: int, r: int, s: List[str]) -> bool:
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1

                else:
                    return False

            return True

        l = 0
        r = len(s) - 1


        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l + 1, r, s) or is_palindrome(l, r - 1, s)

            else:
                l += 1
                r -= 1

        return True