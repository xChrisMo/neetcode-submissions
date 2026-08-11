import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min = 1
        # max = max(piles)

        # condition to close right boundary
        def condition(i):
            days = 0
            for pile in piles:
                days += math.ceil(pile / i)
                if days > h:
                    return False


            return True

        l = 1
        r = max(piles)

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m 

            else:
                l = m + 1


        return l