from heapq import heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # heapq.heapify(nums)
        # while len(nums)>k:
        #     heapq.heappop(nums)
        # return nums[0]
        nums.sort()

        for  i in range(len(nums)-1,-1,-1):
            k-=1
            if k==0:
                return nums[i]

            

