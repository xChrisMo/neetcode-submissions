class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i, num in enumerate(nums):
            print(left_sum)
            print(right_sum)
            
            if left_sum == right_sum - num:
                return i

            left_sum += num
            right_sum -= num


        return -1