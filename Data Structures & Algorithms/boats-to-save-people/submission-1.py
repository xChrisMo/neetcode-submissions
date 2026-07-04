class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # we optimise for the heav people basically
        people.sort()
        count = 0

        l = 0
        r = len(people) - 1


        while l <= r:
            remaining = limit - people[r]
            count += 1

            if people[l] <= remaining:
                l += 1

            r -= 1

        return count

