class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        start = prices[0]

        for price in prices[1:]:
            if price >= start:
                max_p += (price - start)

            start = price

        return max_p
            