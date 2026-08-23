class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        {xyz}
        '''
        charset=set()
        maxVal=0
        l=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            maxVal=max(maxVal,r-l+1)
        return maxVal
            
