import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cond(k):
            time_taken=0
            for pile in piles:
                time_taken+=math.ceil(pile/k)
            return time_taken<=h

        
        l=1
        r=max(piles)
        while l<r:
            m=l+((r-l)//2)
            if cond(m):
                r=m
            else:
                l=m+1
        print(l)
        return l
        
        
