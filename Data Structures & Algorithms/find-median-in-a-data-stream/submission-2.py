from heapq import heappop, heappush
class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap

    def addNum(self, num: int) -> None:
        # we need to make sure abs(len(small)-len(large)) < 2
        # we have to make sure max from small < min from large
        if self.large and num > self.large[0]:
            heappush(self.large, num)

        else:
            heappush(self.small, -num)
        
        if len(self.small) - len(self.large) > 1:
            # if greater
            val = heappop(self.small)
            heappush(self.large, -val)

        elif len(self.large) - len(self.small) > 1:
            # if greater
            val = heappop(self.large)
            heappush(self.small, -val)

        # while max from self.small >= min from self.large
        # val = heappop(self.small)
        # heappush(self.large, -val)

        # # while min from self.large < max from self.small
        # val = heappop(self.large)
        # heappush(self.small, val)

        # else just heappush into self.small

    def findMedian(self) -> float:
        i = len(self.small)
        j = len(self.large)
        
        # if same size
        # remember large is a minheap, 
        # so small which is a large heap has all the negative

        if i == j:
            return ((-1 * self.small[0]) + self.large[0]) / 2
        
        else:
            if i > j:
                return float(-1 * self.small[0])

            else:
                return float(self.large[0]) 

        # 