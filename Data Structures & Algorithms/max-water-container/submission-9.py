class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        
        [1,7,2,5,4,7,3,6]
        '''
        l=0
        r=len(heights)-1
        maxVal=0
        while l<r:
            area=(r-l)*min(heights[l],heights[r])
            if area>maxVal:
                maxVal=area
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        print(maxVal)
        return maxVal
        