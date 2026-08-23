class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        matches 26
        a1   a1
        b 1  b1
        c  1 c1
            e
            l 

            {0}
        '''
        if len(s1)>len(s2):
            return False
        map1={}
        map2={}
        for i in range(26):
            map1[i]=0
            map2[i]=0
        for i in range(len(s1)):
            map1[ord(s1[i])-ord("a")]=1+map1.get(ord(s1[i])-ord("a"),0)
            map2[ord(s2[i])-ord("a")]=1+map2.get(ord(s2[i])-ord("a"),0)
        print(map1,map2)
        matches =0
        for i in range(26):
            matches+=(1 if map1[i]==map2[i] else 0)
        print(matches)

        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            index=ord(s2[r])-ord("a")
            map2[index]+=1
            if map2[index]==map1[index]:
                matches+=1
            elif map2[index]==map1[index]+1:
                matches-=1
            index_l=ord(s2[l])-ord("a")
            map2[index_l]-=1
            if map2[index_l]==map1[index_l]:
                matches+=1
            elif map2[index_l]+1==map1[index_l]:
                matches-=1
            l+=1
        return matches ==26

        