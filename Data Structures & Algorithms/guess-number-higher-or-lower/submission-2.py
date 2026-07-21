# The guess API is already defined for you.
# @param num, your guess
# @return -1 if guess is higher than the picked number
#          1 if guess is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n + 1

        while l < r:
            m = l + (r - l) // 2

            if guess(m) <= 0:
                r = m

            else:
                l = m + 1

        
        return l