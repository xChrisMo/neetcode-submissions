class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax=[0]
        
        '''
        
        [0,2,0,3,1,0,1,3,2,1]
        []
        rightMax=[]
        for i in range(1,len(height)):
            maxL=max(height[:i])
            leftMax.append(maxL)
        for i in range(1,len(height)):
            maxRight=max(height[i:])
            rightMax.append(maxRight)
        rightMax.append(0)
        res=0
        for i in range(len(height)):
            val=min(leftMax[i],rightMax[i])-height[i]
            if val<0:
                val=0
            res+=val

        print(res)
        return res
    
        '''
        l=0
        r=len(height)-1
        leftMax=height[l]
        rightMax=height[r]
        res=0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                res+=(leftMax-height[l])
            else:
                r-=1
                rightMax=max(rightMax, height[r])
                res+=(rightMax-height[r])
        return res
        