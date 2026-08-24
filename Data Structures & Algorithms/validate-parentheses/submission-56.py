class Solution:
    def isValid(self, s: str) -> bool:
        '''
        [[{)
        '''
        
        dict={")":"(","]":"[","}":"{"}
        stack=[]
        if len(s)%2!=0:
            return False

        for ele in s:
            if ele in dict and stack:
                if dict[ele]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ele)
        return True if not stack else False
                
            
        
        
        