from heapq import heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sofrt from letgest to smallest
        # so build a max heap
        # then pop tilll we get to k

        min_heap = []

        for num in nums: #o(n)
            heappush(min_heap, -1 * num) # o(logn) 

        i = 1

        while i < k:
            heappop(min_heap) # log n 
            i += 1
        
        return -1 * min_heap[0]