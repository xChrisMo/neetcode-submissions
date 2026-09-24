class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows= len(matrix)
        cols=len(matrix[0])
        
        #perform BS on the matrix to get teh right row first
        l=0
        r=rows-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]>target:
                
                r=m-1
            elif matrix[m][-1]<target:
                l=m+1
            else:
                break
        midpoint=(l+r)//2

        left=0
        right=cols-1
        while left<=right:
            m=left+ ((right-left)//2)
            if matrix[midpoint][m]<target:
                left=m+1
            elif matrix[midpoint][m]>target:
                right=m-1
            else:
                return True
        return False



