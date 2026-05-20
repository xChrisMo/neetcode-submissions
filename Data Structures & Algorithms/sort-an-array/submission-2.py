class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort_array(num):
            n = len(num) 
            if n < 2:
                return num

            mid = n // 2

            left = num[:mid]
            right = num[mid:]

            return merge_arr(sort_array(left), sort_array(right))

        def merge_arr(l1, l2):
            out = []
            i = j = 0

            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    out.append(l1[i])
                    i += 1

                else:
                    out.append(l2[j])
                    j += 1

            out.extend(l1[i:])
            out.extend(l2[j:])

            return out

        return sort_array(nums)