import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        [-2,-3,-6,-2,-4]
         -6
        -4 -3
        -2 -2
        
        '''
        newStones=[-s for s in stones]
        heapq.heapify(newStones)
        while len(newStones)>1:
            first= heapq.heappop(newStones)
            second= heapq.heappop(newStones)
            if first<second:
                heapq.heappush(newStones,first-second)
        
        return abs(newStones[0]) if newStones else 0
        