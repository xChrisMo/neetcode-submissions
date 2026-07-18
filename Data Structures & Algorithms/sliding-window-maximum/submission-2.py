class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        # while size of queue >  k, pop l! move l (only time we do)
        # while num > nums[q[-1]], q.pop()
        # out.append(nums[q[0]])
        
        
        # return out
        l = 0
        r = 0
        out = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop() #remove all the seen elements (FROM THE RIGHT)
            
            # why do we append after this ?? or is it just the normal appending...
            q.append(r)

            # i do not get the reason for this at allll, this l > q[0] ?
            if l > q[0]:
                q.popleft()

            # so also this, should we not be checking if r + 1 == k ?
            # i dont understand how r + 1 is able to account for the entire range
            # what if we never moved l ? then that is going to be greater than k, no ??
            # why do we move l simply because we added ??

            if (r + 1) >= k:
                out.append(nums[q[0]])
                l += 1
            
            r += 1


        return out

            

            