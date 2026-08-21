class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        [1,2,3,4] #3
        '''
        l=0
        r=len(numbers)-1
        while l<r:
            sum=numbers[l]+numbers[r]
            if sum>target:
                r-=1
            elif sum<target:
                l+=1
            else:
                print([l,r])
                return [l+1,r+1]