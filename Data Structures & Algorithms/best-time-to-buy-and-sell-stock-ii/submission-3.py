class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # take a forward scan, compare minimum to next greater time?
        # we can only hold max of one share of stock 
        max_price = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_price += (prices[i] - prices[i - 1] )

        return max_price