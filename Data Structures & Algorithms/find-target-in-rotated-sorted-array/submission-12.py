class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        def condition(m, r):
            return nums[m] < nums[r]

        l = 0 
        r = n 

        def middle_search(l, r) -> int:
            while l < r:
                m = l + (r - l) // 2
                
                if condition(m, r):
                    r = m 

                else:
                    l = m + 1
                    

            return l 

        
        pivot = middle_search(l, r)
        
        def binary_search(l, r, target):
            while l <= r:
                m = l + (r - l) // 2

                if nums[m] == target:
                    return m

                elif nums[m] > target:
                    r = m - 1

                else:
                    l = m + 1

            return -1

        left_search = binary_search(0, pivot - 1, target)
        right_search = binary_search(pivot, n, target)

        if left_search != -1:
            return left_search

        
        if right_search != -1:
            return right_search

        return -1

        

