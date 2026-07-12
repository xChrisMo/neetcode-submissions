class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # due to the size we recurisvly do a merge sort. like a divide and conqyer thing

        def sort_arr(nums):
            if len(nums) <= 1:
                return nums

            m = len(nums) // 2
            left = sort_arr(nums[:m])
            right = sort_arr(nums[m:])

            out = merge_arr(left, right)
            return out

        def merge_arr(left, right):
            out = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    out.append(left[i])
                    i += 1

                else:
                    out.append(right[j])
                    j += 1

            out.extend(left[i:])
            out.extend(right[j:])

            return out

        return sort_arr(nums)