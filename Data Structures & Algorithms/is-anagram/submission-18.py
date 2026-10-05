from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_s= Counter(s)
        count_t=Counter(t)

        for ele in s:
            if count_s[ele]!=count_t.get(ele,0):
                return False
        return True
        