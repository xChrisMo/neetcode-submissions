class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # prices.sort()

        # if prices[0] + prices[1] > money:
        #     return money 

        # else:
        #     return money - prices[0] - prices[1]

        #o(n log n) time
        #o(1) space

        min_1 = min_2 = float('inf')

        for price in prices:
            if price < min_1:
                min_2 = min_1
                min_1 = price
            else:
                min_2 = min(price, min_2)

        choc = money - min_1 - min_2    
        if choc < 0: 
            return money
        return choc