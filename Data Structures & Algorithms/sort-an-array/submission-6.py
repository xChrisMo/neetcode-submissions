class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # divide and conquer to be fair. 
        # if len(nums) == 1, base condition, return nums[0]
        # break it down, find the middle point
        # m = len(nums) // 2
        # left = nums[:m]
        # right = nums[m:]

        def merge(nums):
            if len(nums) < 2:
                return nums

            mid = len(nums) // 2
            left = merge(nums[:mid])
            right = merge(nums[mid:])

            return merge_sort(left, right)
        # inside merge, take 2 arrays

        # out = []
        # i = j = 0
        # while i < len(arr_a) and j < len(arr_b)
        # add littler one, if equal i'd choose to add b
        # extend in case we break out of while loop
        # return out 

        def merge_sort(left_arr, right_arr):
            out = []
            i = j = 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    out.append(left_arr[i])
                    i += 1

                else:
                    out.append(right_arr[j])
                    j += 1

            out.extend(left_arr[i:])
            out.extend(right_arr[j:])

            return out

        return merge(nums)
        

