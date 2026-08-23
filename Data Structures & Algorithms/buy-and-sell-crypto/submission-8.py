class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        double for loop
        maxP=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                maxP=max(maxP,profit)
        print(maxP)
        return maxP
        prices=[5,1,5,6,7,1,10]
        maxP=6
        '''

        l=0
        r=1
        maxP=0
        while r<len(prices):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                maxP=max(maxP,profit)
                
            else:
                l=r
            r+=1
        print(maxP)
        return maxP
            



        