from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res= {}

        for st in strs:
            count=[0]*26
            tmp=[]
            for ele in st:
                count[ord(ele)-ord("a")]+=1
            if tuple(count) not in res:
                tmp.append(st)
                res[tuple(count)]=(tmp)
            else:
                res[tuple(count)].append(st)
        

            
        # print(res.values())
        return list(res.values())


