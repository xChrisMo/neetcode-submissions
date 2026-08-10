class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        min_price = prices[0]

        for price in prices[1:]:
            if price > min_price:
                res += price - min_price
            min_price = price
            

        return res