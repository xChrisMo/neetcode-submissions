class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #return s2 in s1
        # make s1 and s2 into a list, sort them both. then keep a window of size s1 as we iterate ?

        # Input: s1 = "abc", s2 = "lecabee"

        # make s1 a list, make s2 a dict
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2: return False

        l_s1 = [0] * 26
        l_s2 = [0] * 26

        
        for i in range(n1):
            l_s1[ord(s1[i]) - ord('a')] += 1
            l_s2[ord(s2[i]) - ord('a')] += 1

        # early check 
        if l_s1 == l_s2: 
            return True

        for i in range(n1, n2): #basically considering all other spaces
            # add
            l_s2[ord(s2[i]) - ord('a')] += 1

            # remove
            l_s2[ord(s2[i - n1]) - ord('a')] -= 1

            if l_s1 == l_s2:
                return True

        return False