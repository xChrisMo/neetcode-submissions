class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        i=1
        stack=[[38,1][36,3][35,4]]
        [30,38,30,36,35,40,28]
        [1010100]
        '''
        stack=[]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):

            while stack and t>stack[-1][0]:
                val,indx=stack.pop()
                res[indx]=i-indx

            stack.append([t,i])
        # print(res)
        return res
        