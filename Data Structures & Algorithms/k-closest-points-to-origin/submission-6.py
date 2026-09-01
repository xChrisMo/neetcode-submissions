import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        look for the distance between the points
        '''
        res=[]
        for x,y in points:
            dist=x**2 + y**2
            res.append([dist,x,y])
        heapq.heapify(res)

        ans=[]
        while k>0:
            tmp=heapq.heappop(res)
            dist,x,y=tmp
            ans.append([x,y])
            k-=1
        # print(ans)
        return ans
        
