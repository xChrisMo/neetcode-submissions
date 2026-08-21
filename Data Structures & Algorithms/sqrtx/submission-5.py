class Solution:
    def mySqrt(self, x: int) -> int:

        def cond(k):
            return k*k>x
        l=1
        r=x+1
        while l<r:
            m=(l+r)//2

            if cond(m):
                r=m
            else:
                l=m+1
        return l-1
         

        
