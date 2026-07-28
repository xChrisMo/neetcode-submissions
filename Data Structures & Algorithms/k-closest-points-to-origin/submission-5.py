from heapq import heappop, heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points i = x1, y1
        # integer k!

        # k closest to origin
        # eclidian distance = '/((x1-x2)**2 + (y1-y2)**2)

        # preprocess point, get ec distance, addd it as first element inside a tyuple
        # add each tuple into a min_heap, and the while len(out) < k, pop k times!

        min_heap = []

        def euclidian_distance(point: List[int]) -> Tuple(int): #o(1) time
            y2 = point[1]
            x2 = point[0]

            diff = ((x2)** 2 + (y2)**2) ** 0.5
            return (diff, [x2, y2])

        for point in points:
            heappush(min_heap, euclidian_distance(point)) #o(n)

        
        out = []
        
        while len(out) < k:
            point= heappop(min_heap) #o(logk)
            out.append(point[1])

        return out

        # so o(klogn) time. in the worst case, we do logn K times
        # o(1) space