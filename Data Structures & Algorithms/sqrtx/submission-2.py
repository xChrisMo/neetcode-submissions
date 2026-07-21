class Solution:
    def mySqrt(self, x: int) -> int:
        # find the largest integr whose sqaure is less than x
        # we want a range from 0 to half of that number !
        # our condition would be, if if square of that index >= x, right = mid
        # else, l = m + 1


        def condition(i):
            return i * i > x
            # this is looking for all indices greater or equal to x
            # else we move l!
            

        l = 0
        r = x + 1

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m

            else:
                l = m + 1

        return l - 1

        # 13
        # 0, 1, 2, 3, 4, 5, 6
        # m = 3
