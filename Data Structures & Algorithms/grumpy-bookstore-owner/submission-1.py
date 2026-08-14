class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        currnet_window = 0
        always_satisfied = 0
        max_bonus = 0
        l = 0
        n = len(customers)

        for r in range(n):
            if grumpy[r] == 0:
                always_satisfied += customers[r]
            else:
                currnet_window += customers[r]

            while r - l + 1 > minutes:
                if grumpy[l] == 1:
                    currnet_window -= customers[l]
                l += 1

            max_bonus = max(max_bonus, currnet_window)

        return max_bonus + always_satisfied