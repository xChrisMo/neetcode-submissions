class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return True if s2 contains s1
        # so we would use two lists
        # abd a sliding window! 

        # from l to r, 
        # if for a window, array[s1] == array[s2]: return True
        # else: move forward, add r to the list, remove left!  make sure len s1 is the metric

        # off the bat if len(s1) > len(s2): return False!
        if len(s1) > len(s2): return False

        check = [0] * 26

        for char in s1:
            check[ord(char) - ord('a')] += 1

        l = 0 

        base = [0] * 26
        
        for r in range(len(s2)):

            base[ord(s2[r]) - ord('a')] += 1
            
            while r - l + 1 > len(s1):
                base[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if check == base:
                return True

        return False