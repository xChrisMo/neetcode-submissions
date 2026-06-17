class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #initial max = -1
        # reverse iteration
        # newmax = max(oldmax, arr[i])
        oldmax = -1
        for i in range(len(arr)-1,-1,-1):
            newmax = max(oldmax,arr[i])
            arr[i] = oldmax
            oldmax= newmax
        return arr
        

        