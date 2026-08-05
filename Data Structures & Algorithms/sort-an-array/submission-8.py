class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # we recursively break down each element into bits
        # if len(word) == 1, we return word
        # else we recursively build up

        # merge function
        # recursive breakdown
        # if terminal, we return value
        # we call the sort function
        # return merged value

        # sort function
        # compares two values with 1 out
        # if one finishes, we extend the other, vice versa
        # return sorted value

        def merge(arr):
            n = len(arr)

            if len(arr) < 2:
                return arr
            
            left = merge(arr[:n//2])
            right = merge(arr[n//2:])

            return sort_arr(left, right)

        def sort_arr(left_arr, right_arr):
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