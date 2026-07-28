from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [x,y,z]
        # take largest 2
        # if x == y, both destroyed
        # if if x < y, x = 0, y -= x
        

        # build a max heap off nums
        # run simulation while len(heap) > 1
        # return only element remaining

        max_heap = []

        for stone in stones:
            heappush(max_heap, -1 * (stone))

        while len(max_heap) > 1:
            largest = heappop(max_heap)
            second = heappop(max_heap)

            if largest == second:
                heappush(max_heap, 0)

            # -3, -2
            else:
                heappush(max_heap, largest - second)

        return -1 * max_heap[0]