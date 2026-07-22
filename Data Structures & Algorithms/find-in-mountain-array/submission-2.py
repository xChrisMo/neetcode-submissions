class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # try to find peak, 
        # from left to peak, do bs
        # from peak to right, do bs

        # both sides of peak are sorted, 
        # left to peak -- ascending
        # peak to right -- descending

        # [1,2,3,4,2,1]
        # l = 0
        # r = 5
        # m = 2
        # true (move right), would mean, we have seen nums[i - 1] < nums[i] > nums[i + 1]
        # the question is, are we always guaranteed to see this ??

        def condition(i):
            return mountainArr.get(i) > mountainArr.get(i + 1)


        l = 0 
        r = mountainArr.length() - 1

        start = l 
        end = r

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m 

            else:
                 l = m + 1

        # this should return the peak element because we keep moving leftmost !

        peak = l

        # now we try bs between start and peak, and also between peak and end

        # so now we try find the leftmost element that satisfy the condition of >= 

        # for left to peak, from start to peak
        
        def condition_lp(i):
            return mountainArr.get(i) >= target

        l = start
        r = peak

        while l < r:
            m = l + (r - l) // 2

            if condition_lp(m):
                r = m

            else:
                l = m + 1

        # this is the closest to what what we are looking for, but it isnt it 
        if mountainArr.get(l) == target:
            return l


        #################################################################################################################################################################

        
        # for peak to right, from peak to end
        
        def condition_pr(i):
            return mountainArr.get(i) <= target

        l = peak
        r = end

        while l < r:
            m = l + (r - l) // 2

            if condition_pr(m):
                r = m

            else:
                l = m + 1

        # this is the closest to what what we are looking for, but it isnt it 
        if mountainArr.get(l) == target:
            return l


        return -1
        

