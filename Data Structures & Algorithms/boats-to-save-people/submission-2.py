class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()

        # [1, 2, 2, 3, 3]

        l = 0
        r = len(people) - 1


        while l <= r:
            if people[r] + people[l] <= limit:
                l += 1

            count += 1
            r -= 1

        return count 