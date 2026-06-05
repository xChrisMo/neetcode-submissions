class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n 
        right = -1

        for i in range(n-1, -1, -1):
            ans[i] = right 
            right = max(arr[i], right)
        return ans
