class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
         [2,20,4,10,3,4,5]
        '''
        longest=0
        setNum=set(nums)

        for num in setNum:

            if num-1 not in setNum:
                length=0
                while (num+length) in setNum:
                    length+=1
                # longest=max(longest,length)
                if length>longest:
                    longest=length
        print(longest)
        return longest

                