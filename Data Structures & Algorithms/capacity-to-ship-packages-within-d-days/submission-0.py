class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # carry max?
        # max_weight

        total_weight = sum(weights)
        max_weight = max(weights)

        def condition(capacity):
            # we want to start at a day, 
            # iif we exceed the current capacity, day += 1
            # capacity = cyrrent weight
            # if days > DAYS:
            # return False
            # else, return True!

            dday = 1
            total = 0

            for weight in weights:
                total += weight

                if total > capacity:
                    dday += 1
                    total = weight # resetting this guy
                    if dday > days:
                        return False

            return True


        l = max_weight
        r = total_weight


        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m

            else:
                l = m + 1

        
        return l