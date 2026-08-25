from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        resLen=float("inf")
        res=[-1,-1]
        needMap=Counter(t)
        haveMap={}
        need=len(needMap)
        have=0
        l=0
        for r in range(len(s)):
            cur=s[r]
            haveMap[cur]=1+haveMap.get(cur,0)
            if cur in needMap and haveMap[cur]==needMap[cur]:
                have+=1
            while have ==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                haveMap[s[l]]-=1
                if s[l] in needMap and  haveMap[s[l]]<needMap[s[l]]:
                    have-=1
                l+=1
        l,r=res   
        return s[l:r+1]  if resLen!= float("inf") else   ""         


      

        