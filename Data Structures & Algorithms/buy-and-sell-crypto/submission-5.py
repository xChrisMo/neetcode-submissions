class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # from 0 to n - 1
        # we want to find the minimum, 
        ans = 0

        min_p = float('inf')
        n = len(prices)

        for r in range(n):
            min_p = min(min_p, prices[r])
            ans = max(ans, prices[r] - min_p)

        return ans