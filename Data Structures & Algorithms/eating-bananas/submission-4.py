import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h -> hours to eat ALL bananas
        # the range of time we need is 
        # 1 to max(piles)


        # q1: 1 to 4
        # q2: 1 to 25


        # hours = 1, if 
        # for each hour, if hour % time != 0, math.ceil(), add to hours 

        def condition(speed):
            # we start frpm day 1
            hours = 0
            # 
            for pile in piles:
                hours += math.ceil(pile / speed)
                
                if hours > h: # no need to wait till the end, we know it is too much, it exceeds h!
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