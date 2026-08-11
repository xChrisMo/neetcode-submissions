import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # min = max(weights)
        # max = sum(weights)

        # conditiion to move right
        def condition(m):
            count = 1
            total = 0

            for w in weights:
                total += w
                
                if total > m:
                    count += 1
                    total = w
                    if count > days:
                        return False

            return True


        l = max(weights)
        r = sum(weights)

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m 

            else:
                l = m + 1

        return l